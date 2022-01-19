import math

def divide_and_conquer(a , n):
    mult = 1
    if 1 == n:
        return a
    else:
        mult *= divide_and_conquer(a, math.floor(n/2))
        mult *= divide_and_conquer(a , math.ceil(n/2))

    return mult

def brute_force(a , n):
    mult = 1

    for i in range(0,n):
        mult *= a

    return mult

a = 6
n = 2
print(a , "*" , n ,"calculated by using divide and conquer =",divide_and_conquer(a,n))
print(a , "*" , n ,"calculated by using brute force =",brute_force(a,n))
