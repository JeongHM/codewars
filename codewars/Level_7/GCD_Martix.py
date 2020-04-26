import math

def gcd_matrix(a,b):
    answer = [gcd(i, j) for j in b for i in a]
    return round(sum(answer) / len(answer), 4)


def gcd(a, b):
    if b == 0:
        return None

    while (b != 0):
        c = a % b
        a = b
        b = c
    return abs(a)



# Other Solution
# from math import gcd

# def gcd_matrix(a, b):
#     return round(sum(gcd(m, n) for m in a for n in b) / (len(a) * len(b)), 3)
