// C++ program to demonstrate
// working of LIFO
// using stack in C++
// Available at: https://www.geeksforgeeks.org/lifo-last-in-first-out-approach-in-programming/

#include<bits/stdc++.h>
using namespace std;
 
// Pushing element on the top of the stack
stack<int> stack_push(stack<int> stack)
{
    for (int i = 0; i < 5; i++)
    {
        stack.push(i);
    }
    return stack;
}
 
// Popping element from the top of the stack
stack<int> stack_pop(stack<int> stack)
{
    cout << "Pop :";
 
    for (int i = 0; i < 5; i++)
    {
        int y = (int)stack.top();
        stack.pop();
        cout << (y) << endl;
    }
    return stack;
}
 
// Displaying element on the top of the stack
void stack_peek(stack<int> stack)
{
    int element = (int)stack.top();
    cout << "Element on stack top : " << element << endl;
}
 
// Searching element in the stack
void stack_search(stack<int> stack, int element)
{
    int pos = -1,co = 0;
    while(stack.size() > 0)
    {
        co++;
        if(stack.top() == element)
        {
            pos = co;
            break;
        }
        stack.pop();
    }
 
    if (pos == -1)
        cout << "Element not found" << endl;
    else
        cout << "Element is found at position " << pos << endl;
}
 
// Driver code
int main()
{
    stack<int> stack ;
 
    stack = stack_push(stack);
    stack = stack_pop(stack);
    stack = stack_push(stack);
    stack_peek(stack);
    stack_search(stack, 2);
    stack_search(stack, 6);
    return 0;
}
     
// This code is contributed by Arnab Kundu
