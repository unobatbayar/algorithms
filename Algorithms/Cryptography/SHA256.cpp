//
//    Author: patrick garnaut
//        Date: AUG-2010
//        
//    SHA256 message digest implementation.
//    Probably slow, buggy and bloated, but this was a learning exercise. 
//


#include <string.h>
#include <stdlib.h>

#include "sha256.h"

// (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311):
const uint32 K[64] = {  
0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
};


// get big-endian 32bit value
// called a LOT - hence inlined
#define GET_BE_UINT32(n,b,i)\
{\
    (n) = ((uint32)(b)[(i)] << 24)\
        | ((uint32)(b)[(i) + 1] << 16)\
        | ((uint32)(b)[(i) + 2] <<  8)\
        | ((uint32)(b)[(i) + 3]);\
}
// shift right
#define  RSHIFT(x,n) ((x & 0xFFFFFFFF) >> n)
// right rotation
#define RROT(x,n) (RSHIFT(x,n) | (x << (32 - n)))
//
#define XOR ^

void Sha256Digest::reset() {
    m_total[0] = 0;
    m_total[1] = 0;
    // initial values from the SHA-256 spec
    // (first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19):
    m_state[0] = 0x6A09E667;
    m_state[1] = 0xBB67AE85;
    m_state[2] = 0x3C6EF372;
    m_state[3] = 0xA54FF53A;
    m_state[4] = 0x510E527F;
    m_state[5] = 0x9B05688C;
    m_state[6] = 0x1F83D9AB;
    m_state[7] = 0x5BE0CD19;
    m_bufferFilled = 0;
    m_msgLength = 0;
}

// process 64 byte chunk
// translated from pseudocode on wikipedia
void Sha256Digest::process() {
    // these follow the naming conventions in the psuedocode
    uint32 w[64];
    uint32 a, b, c, d, e, f, g, h;
    uint32 s0, s1, maj, t2, t1, ch;
    
    GET_BE_UINT32(w[0], m_buffer, 0);
    GET_BE_UINT32(w[1], m_buffer, 4);
    GET_BE_UINT32(w[2], m_buffer, 8);
    GET_BE_UINT32(w[3], m_buffer, 12);
    GET_BE_UINT32(w[4], m_buffer, 16);
    GET_BE_UINT32(w[5], m_buffer, 20);
    GET_BE_UINT32(w[6], m_buffer, 24);
    GET_BE_UINT32(w[7], m_buffer, 28);
    GET_BE_UINT32(w[8], m_buffer, 32);
    GET_BE_UINT32(w[9], m_buffer, 36);
    GET_BE_UINT32(w[10], m_buffer, 40);
    GET_BE_UINT32(w[11], m_buffer, 44);
    GET_BE_UINT32(w[12], m_buffer, 48);
    GET_BE_UINT32(w[13], m_buffer, 52);
    GET_BE_UINT32(w[14], m_buffer, 56);
    GET_BE_UINT32(w[15], m_buffer, 60);

    // init hash value for this chunk
    a = m_state[0];
    b = m_state[1];
    c = m_state[2];
    d = m_state[3];
    e = m_state[4];
    f = m_state[5];
    g = m_state[6];
    h = m_state[7];

    for(int i=16; i<64; i++) {
        s0 = RROT(w[i-15], 7) XOR RROT(w[i-15], 18) XOR RSHIFT(w[i-15], 3);
        s1 = RROT(w[i-2], 17) XOR RROT(w[i-2], 19) XOR RSHIFT(w[i-2], 10);
        w[i] = w[i-16] + s0 + w[i-7] + s1;
    }

    // main loop
    // TODO: unroll?  
    for(int j=0; j<64; j++) {
        s0 = RROT(a, 2) XOR RROT(a, 13) XOR RROT(a, 22);
        maj = (a & b) XOR (a & c) ^ (b & c);
        t2 = s0 + maj;
        s1 = RROT(e, 6) XOR RROT(e, 11) XOR RROT(e, 25);
        ch = (e & f) XOR ((~e) & g);
        t1 = h + s1 + ch + K[j] + w[j];
        
        h = g;
        g = f;
        f = e;
        e = d + t1;
        d = c;
        c = b;
        b = a;
        a = t1 + t2;
    }
    
    // append this chunk's has value
    m_state[0] += a;
    m_state[1] += b;
    m_state[2] += c;
    m_state[3] += d;
    m_state[4] += e;
    m_state[5] += f;
    m_state[6] += g;
    m_state[7] += h;
}

// big endian
// called only once in finalise() - no need to inline it
static void packUint64(uint8 *buf, uint64 val) {
    buf[7] = (uint8)val;
    buf[6] = (uint8)(val >> 8);
    buf[5] = (uint8)(val >> 16);
    buf[4] = (uint8)(val >> 24);
    buf[3] = (uint8)(val >> 32);
    buf[2] = (uint8)(val >> 40);
    buf[1] = (uint8)(val >> 48);
    buf[0] = (uint8)(val >> 56);
}

// this deviates slightly from the wiki pseudocode - because we dont want to pad more than we have to.
// consider calling update on two separate 32byte inputs ...
void Sha256Digest::update(uint8 *input, uint32 length) {
    uint32 available = 64 - m_bufferFilled;
    if(length <= 0)
        return;
    
    m_msgLength += length;
    
    if(length < available) {
        memcpy(&m_buffer[m_bufferFilled], input, length);
        m_bufferFilled += length;
        return;
    }
    if(length == available) {
        memcpy(&m_buffer[m_bufferFilled], input, length);
        m_bufferFilled = 0;
        process();
        return;
    }
    
    // have lots of input...
    // fill the remainder of the buffer and process
    memcpy(&m_buffer[m_bufferFilled], input, available);
    process();
    length -= available;
    input += available;
    
    // do 64 bit chunks
    while(length >= 64) {
        memcpy(m_buffer, input, 64);
        process();
        length -= 64;
        input += 64;
    }
    m_bufferFilled = 0;

    // do any left overs
    if(length > 0) {
        memcpy(m_buffer, input, length);
        m_bufferFilled = length;
    }  
}
void Sha256Digest::padAndFinalize() {
    if(m_bufferFilled == 0) {
        // need to pad out a whole new 64byte chunk and process it
        m_buffer[m_bufferFilled] = 1 << 7;
        memset(&m_buffer[m_bufferFilled + 1], 0, 55);
        packUint64(&m_buffer[56], m_msgLength * 8);
    }
    else if(m_bufferFilled < 56) {
        // need to pad out somewhere between 1 and 55 bytes (including msgLen string) ...
        sint32 paddingSize = 56 - m_bufferFilled;
        m_buffer[m_bufferFilled] = 1 << 7;
        memset(&m_buffer[m_bufferFilled + 1], 0, paddingSize - 1);
        packUint64(&m_buffer[m_bufferFilled + paddingSize], m_msgLength * 8);
    }
    else if(m_bufferFilled == 56) {
        // pad with 80 00 00 00 00 00 etc. then do another run with buffer set to 00 00 00 ... 00 <input size>
        m_buffer[m_bufferFilled] = 1 << 7;
        memset(&m_buffer[m_bufferFilled + 1], 0, 7);
        process();
            
        memset(m_buffer, 0, 56);
        packUint64(&m_buffer[56], m_msgLength * 8);
    }
    else {
        // 56 < m_bufferFilled < 64
        m_buffer[m_bufferFilled] = 1 << 7;
        memset(&m_buffer[m_bufferFilled + 1], 0, 64 - m_bufferFilled - 1);
        process();

        memset(m_buffer, 0, 56);
        packUint64(&m_buffer[56], m_msgLength * 8);
    }
    process();

}
// big endian
void packUint32(uint8 *buf, uint64 val) {
    buf[3] = (uint8)val;
    buf[2] = (uint8)(val >> 8);
    buf[1] = (uint8)(val >> 16);
    buf[0] = (uint8)(val >> 24);
}

void Sha256Digest::finalise() {
    padAndFinalize();
}

void Sha256Digest::getHash(uint8 digest[32]) {
    for(uint32 i=0; i<8; i++) {
        packUint32(&digest[i * 4], m_state[i]);
    }
}