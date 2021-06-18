def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1] # before arr[i] (arr[i] including), are all smaller than pivot)
    return i+1 # index of pivot



def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1) # quicksort pivot's left
        quickSort(arr, pi+1, high) # quicksort pivot's right
