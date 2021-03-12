def binarySearch(array, item):
    low = 0
    high = len(array)
    if high < 2:
        return 0
    
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == item:
            return mid
        if array[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def binarySearchRecursive(array, low, high, item):
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == item:
            return mid
        elif array[mid] < item:
            return binarySearchRecursive(array, mid + 1, high, item)
        else:
            return binarySearchRecursive(array, low, mid -1, item)
        
    else:
        return -1


arr = [2, 3, 4, 10, 22, 40, 52]
print(binarySearch(arr, 4))
print(binarySearch(arr, 22))
print(binarySearch(arr, 3))

print(binarySearchRecursive(arr, 0, len(arr)-1, 4))
print(binarySearchRecursive(arr, 0, len(arr)-1, 22))
print(binarySearchRecursive(arr, 0, len(arr)-1, 3))
