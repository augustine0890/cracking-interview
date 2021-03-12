def mergeSort(array):
    n = len(array)
    if n < 2:
        return
    mid = n//2
    l = array[:mid]
    r = array[mid:]

    mergeSort(l)
    mergeSort(r)

    merge(array, l, r, len(l), len(r))


def merge(array, l, r, left, right):
    i = j = k = 0
    while i < left and j < right:
        if l[i] < r[j]:
            array[k] = l[i]
            i += 1
        else:
            array[k] = r[j]
            j += 1
        k += 1
        
    while i < left:
        array[k] = l[i]
        k += 1
        i += 1
    while j < right:
        array[k] = r[j]
        k += 1
        j += 1

arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print(arr)

    