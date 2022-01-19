def kth_smallest(success_rates,start,end,k):
    s = partition(success_rates,start, end)
    if s == k - 1:
        print(success_rates[s])
        return success_rates[s]
    elif s > start + k - 1: 
        return kth_smallest(success_rates,start,s-1,k)
    else:
        return kth_smallest(success_rates,s+1,end,k)

def partition(arr, start , end):
    p = arr[end]
    i = (start - 1)
    for j in range(start, end):
        if arr[j] <= p:
            i = i + 1
            swap(arr, j , i)
    swap(arr, end , i+1)
    return (i+1)

def swap(arr, x , y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

success_rates = [50,10,90,14,67]
k = 5
print(k,"th experiment's success rate is", kth_smallest(success_rates,0,len(success_rates)-1,k))
