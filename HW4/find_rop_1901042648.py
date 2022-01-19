import math 

def mergeSort(arr, n):
    temp = [0] * (n+1)
    return _mergeSort(arr, temp, 0, n) 
 
def _mergeSort(arr, temp, start, end):
    count = 0
 
    if start < end:
 
        mid = math.floor((start+end) / 2)

        count += _mergeSort(arr, temp,start, mid)

        count += _mergeSort(arr, temp,mid + 1, end)
 
        count += merge(arr, temp, start, mid, end)

    return count
 
def merge(arr, temp, start, mid, end):
    i = start   
    j = mid + 1 
    k = start     
    count = 0
 
    while i <= mid and j <= end:
 
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1

        else:
            temp[k] = arr[j]
            count += (mid-i + 1)
            k += 1
            j += 1
 
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
 
    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1
 
    for x in range(start, end + 1):
        arr[x] = temp[x]
 
    return count
 
 
arr = [1, 2, 3, -5]
result = mergeSort(arr, len(arr) - 1)
print("Number of inversions are", result)