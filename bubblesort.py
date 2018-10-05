# sorting algorithm -> bubblesort	
# About bubblesort: Best case O(n), Average O(n2), Worst case O(n2)
# @author unobatbayar


title = 'Welcome to Bubblesort Algorithm!'
print(title + '\n' + 'Enter unsorted data set: ')

user_input = input()
array = user_input.split()

def bubble_sort(array):
    unsorted = True
    while unsorted:
        unsorted = False
        unsorted_last = len(array) -1
        for x in range(unsorted_last):
            if array[x] > array[x+1]:
                array[x],array[x+1] = array[x+1], array[x]
                unsorted = True
    unsorted_last -= 1

bubble_sort(array)
print(array)
