/*
ROT13 algorithm (Rotate by 13 places) / Caesar Cipher derivative

@author unobatbayar
*/
#include <iostream>
#include <cctype>
#include <string>
using namespace std;

string ROT13(string input)
{

    string transformed;
    for (size_t i = 0; i < input.size(); ++i)
    {
        if (isalpha(input[i]))
        {
            if ((tolower(input[i]) - 'a') < 14)
                transformed.append(1, input[i] + 13);
            else
                transformed.append(1, input[i] - 13);
        }
        else
        {
            transformed.append(1, input[i]);
        }
    }
    return transformed;
}

int main()
{
    string input;
    //cout << "Enter plaintext that you would like to use ROT13 on" << endl;
    //cin >> input;
    cout << ROT13("hello") << endl;
    cout << ROT13("uryyb") << endl;
}
