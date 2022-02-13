#include <iostream>
using namespace std;

/**
 * Selection Sort
Worst complexity: n^2
Average complexity: n^2
Best complexity: n^2
Space complexity: 1
**/

int main()
{
    int array[] = {7, 6, 3, 1, 2, 5, 4, 9, 8};
    int size = sizeof(array)/sizeof(array[0]);

    // We find smallest value and place in first index, then repeat from next index
    for(int i = 0; i<size; ++i){
        int smallest = INT_MAX;
        int index = 0;

        // Find smallest value using linear search
        for(int k = i; k<size; ++k){
            if(array[k] < smallest){
                smallest = array[k];
                index = k;
            }
        }
        // Already in position
        if(i == index) continue;

        // Otherwise, swap
        array[index] = array[i];
        array[i] = smallest;

    }

    for(int i = 0; i<size; ++i){
        // Outputs 1 2 3 4 5 6 7 8 9 
        cout << array[i] << ' ';
    }
	return 0;
}
