import math
def candy(prices, n):
    arr = [0 for x in range(n+1)]
    arr[0] = 0
 
    for i in range(1, n+1):
        highest = math.inf * -1
        for j in range(i):
             highest = max(highest, prices[j] + arr[i-j-1])
        arr[i] = highest
 
    return arr[n]
 
prices = [1, 5, 8, 9, 10, 17, 17, 20]
print("Maximum obtainable value is " + candy(prices, len(prices)))