def keyFunc(product):
    return product[1] // product[0]


def cheese(arr, n ,weight):
    totalPrice = 0
    arr.sort(key = keyFunc)
    for i in range(0,n):
        if weight - arr[i][0] >= 0:
            weight -= arr[i][0]
            totalPrice += arr[i][1]
        else:
            totalPrice += arr[i][1] * (weight / arr[i][0])
            weight -= arr[i][0] * (weight / arr[i][0])
            break

    return totalPrice

products = [[20,5],[10,7],[16,10],[22,9],[9,4]]
n = len(products)

print("Maximum price you can get is",cheese(products,n,35), "$")
