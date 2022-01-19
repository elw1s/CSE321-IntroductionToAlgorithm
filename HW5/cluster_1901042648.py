def max_profit(arr,n):
    F = [0] * (n+1)
    F[0] = arr[0]
    print(arr)
    
    for i in range(1,n):
        F[i] = max(arr[i]+F[i-1] , arr[i])
        F[n] = max(F[n], F[i])
        print(arr[i], F[i-1], F[i])

    print(F)
    return F[n]


arr = [3,-5,2,11,-8,9,-5]
print(max_profit(arr,len(arr)))
