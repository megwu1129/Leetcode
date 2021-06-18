def heapify(arr, n, i):
    largest = i # i is the node to heapify down
    l = 2 * i + 1 # left
    r = 2 * i + 2 # right
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i: # do heapify down
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Build a max heap
    for i in range(n//2-1, -1, -1): # last parent is n//2-1
        heapify(arr, n, i) # heapify every node
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap root to end of unsorted part of arr
        heapify(arr, i, 0) # heapify root
