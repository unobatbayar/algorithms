/*
Finds the n-th Fibonacci number using recusion

@author unobatbayar
*/
#include <iostream>
using namespace std;


int fib(int n){
    cout << n << endl; // to semi-visualize the recusive operations
    if (n < 2) return 1;
    return fib(n - 1) + fib(n - 2);
}

int main()
{
    cout << fib(10);
}
