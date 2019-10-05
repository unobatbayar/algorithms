# sorting algorithm -> insertionsort	
# @author unobatbayar


# Data structure	Array
# Worst-case performance	О(n2) comparisons and swaps
# Best-case performance	O(n) comparisons, O(1) swaps
# Average performance	О(n2) comparisons and swaps
# Worst-case space complexity	О(n) total, O(1) auxiliary

# @author unobatbayar

def insertionSort(array): 
    for i in range(1, len(array)): 
        up = array[i] 
        j = i - 1
        while j >=0 and array[j] > up:  
            array[j + 1] = array[j] 
            j -= 1
        array[j + 1] = up      
    return array

array = [10, 9, 8, 7, 6, 5] 
print(insertionSort(array))