/*

Comb sort is a relatively simple sorting algorithm originally designed by Włodzimierz Dobosiewicz and Artur Borowy in 1980, later rediscovered by Stephen Lacey and Richard Box in 1991. Comb sort improves on bubble sort in the same way that Shellsort improves on insertion sort. Wikipedia
Inventor: Wlodzimierz Dobosiewicz, Stephen Lacey, Richard Box
Worst complexity: n^2
Average complexity: n*log(n)
Best complexity: n
Space complexity: 1

*/
// Java program for implementation of Comb Sort
// Available at: https://www.geeksforgeeks.org/comb-sort/
class CombSort
{
	// To find gap between elements
	int getNextGap(int gap)
	{
		// Shrink gap by Shrink factor
		gap = (gap*10)/13;
		if (gap < 1)
			return 1;
		return gap;
	}

	// Function to sort arr[] using Comb Sort
	void sort(int arr[])
	{
		int n = arr.length;

		// initialize gap
		int gap = n;

		// Initialize swapped as true to make sure that
		// loop runs
		boolean swapped = true;

		// Keep running while gap is more than 1 and last
		// iteration caused a swap
		while (gap != 1 || swapped == true)
		{
			// Find next gap
			gap = getNextGap(gap);

			// Initialize swapped as false so that we can
			// check if swap happened or not
			swapped = false;

			// Compare all elements with current gap
			for (int i=0; i<n-gap; i++)
			{
				if (arr[i] > arr[i+gap])
				{
					// Swap arr[i] and arr[i+gap]
					int temp = arr[i];
					arr[i] = arr[i+gap];
					arr[i+gap] = temp;

					// Set swapped
					swapped = true;
				}
			}
		}
	}

	// Driver method
	public static void main(String args[])
	{
		CombSort ob = new CombSort();
		int arr[] = {8, 4, 1, 56, 3, -44, 23, -6, 28, 0};
		ob.sort(arr);

		System.out.println("sorted array");
		for (int i=0; i<arr.length; ++i)
			System.out.print(arr[i] + " ");

	}
}
/* This code is contributed by Rajat Mishra */
