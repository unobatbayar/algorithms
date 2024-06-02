def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    sorted = False
    
    while not sorted:
        # Update the gap value
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            sorted = True
        
        # Perform a single pass with the given gap
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                # Swap elements at i and i + gap
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False  # If a swap occurs, the array is not sorted
            i += 1
    
    return arr

# Example usage:
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = comb_sort(arr)
print(sorted_arr)
