# sorting algorithm -> bucketsort	
# @author unobatbayar


# Data structure Array
# Worst-case performance	O ( n 2 ) {\displaystyle O(n^{2})} O(n^{2})
# Average performance	O ( n + n 2 k + k ) {\displaystyle O(n+{\frac {n^{2}}{k}}+k)} {\displaystyle O(n+{\frac {n^{2}}{k}}+k)}, where k is the number of buckets. O ( n ) , when  k ≈ n {\displaystyle O(n),{\text{when }}k\approx n} {\displaystyle O(n),{\text{when }}k\approx n}.
# Worst-case space complexity	O ( n ⋅ k ) {\displaystyle O(n\cdot k)} 

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
              
def bucketSort(array): 
    arr = [] # empty array
    slot_num = 10 # 10 means 10 slots, each 
                  # slot's size is 0.1 
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in array: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(slot_num): 
        arr[i] = insertionSort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            array[k] = arr[i][j] 
            k += 1
    return array 

title = 'Welcome to BucketSort Algorithm!'
array = [0.12, 0.1, 0.2, 0.5, 0.11, 0.59]  
print("Sorted Array is") 
print(bucketSort(array)) 