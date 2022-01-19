import math

def cutter(n):
    count = 0

    if n == 1:
        return 1
    else:
        count += cutter(math.floor(n/2))
        count += 1

    return count

n = 10
print("Minimum number of cuts needed:",cutter(n))


