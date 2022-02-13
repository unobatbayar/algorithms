#include <iostream>
using namespace std;

/**
 * BubbleSort
 * Worst complexity: n^2
 * Average complexity: n^2
 * Best complexity: n
 * Space complexity: 1
**/

int main()
{
    int arr[] = {7, 6, 3, 1, 2, 5, 4, 9, 8};
    int size = sizeof(arr)/sizeof(arr[0]);

    for(int i = 0; i<size; ++i){
        for(int k = 0; k<size-i; ++k){
            // check if a is bigger than b
            if(arr[k] > arr[k+1]){
                // swap
                int temp = arr[k];
                arr[k] = arr[k+1];
                arr[k+1] = temp;
            }
        }
    }

    for(int i = 0; i<size; ++i){
        // 1 2 3 4 5 6 7 8 9 
        cout << arr[i] << ' ';
    }
	return 0;
}
