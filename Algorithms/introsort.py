def intro_sort(arr):
    max_depth = 2 * (len(arr).bit_length())
    _introsort(arr, 0, len(arr), max_depth)


def _introsort(arr, start, end, max_depth):
    if end - start <= 1:
        return
    
    if max_depth == 0:
        heapsort(arr, start, end)
        return
    
    pivot = partition(arr, start, end)
    _introsort(arr, start, pivot, max_depth - 1)
    _introsort(arr, pivot + 1, end, max_depth - 1)


def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end - 1

    while True:
        while i < end and arr[i] <= pivot:
            i += 1
        while j > start and arr[j] >= pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[start], arr[j] = arr[j], arr[start]
    return j


def heapsort(arr, start, end):
    build_max_heap(arr, start, end)
    for i in range(end - 1, start, -1):
        arr[i], arr[start] = arr[start], arr[i]
        max_heapify(arr, start, i, start)


def build_max_heap(arr, start, end):
    length = end - start
    for i in range(length // 2 - 1, -1, -1):
        max_heapify(arr, start, end, i)


def max_heapify(arr, start, end, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < end and arr[start + left] > arr[start + largest]:
        largest = left
    if right < end and arr[start + right] > arr[start + largest]:
        largest = right

    if largest != i:
        arr[start + i], arr[start + largest] = arr[start + largest], arr[start + i]
        max_heapify(arr, start, end, largest)


# Example usage
numbers = [9, 5, 2, 8, 1, 10]
intro_sort(numbers)
print(numbers)
