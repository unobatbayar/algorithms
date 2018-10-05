# sorting algorithm -> quicksort	
# About quicksort: Average case O(n log n), Worst case O(n2)
# @author unobatbayar
# Thanks to HackerRank's quicksort tutorial

title = 'Welcome to Quicksort Algorithm!'
print(title + '\n' + 'Enter unsorted data set: ')

user_input = input()
array = user_input.split()

def partition(array, left, right, pivot):
    while(left <= right):
        while(array[left] < pivot):
            left += 1
        while(array[right] > pivot):
            right -= 1
        if (left <= right):
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left


def quick_sort(array, left, right):
    if(left >= right):
       return
    pivot = array[(left+right)//2] #reason why we '//' is because it's floor division, in Python 3.x '/' this indicates true division
    index = partition(array, left, right, pivot)
    quick_sort(array, left, index - 1)
    quick_sort(array, index, right)




quick_sort(array, 0, len(array) - 1)
print(array)