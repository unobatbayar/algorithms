# sorting algorithm -> mergesort	
# About mergesort: Best case O(n log n), Average case O(n log n), Worst case O(n log n)
# @author unobatbayar
# Thanks to HackerRank's mergesort tutorial

title = 'Welcome to Mergesort Algorithm!'
print(title + '\n' + 'Enter unsorted data set: ')

user_input = input()
array = user_input.split()

def merge_halves(array, left, end):
    

def merge_sort(array, start, end):
    if (start >= end):
        return
    middle = (start + end)//2
    merge_sort(array, start, middle)
    merge_sort(array, middle + 1, end)
    merge_halves(array, left, end)    


merge_sort(array, 0, len(array) - 1)
print(array)

