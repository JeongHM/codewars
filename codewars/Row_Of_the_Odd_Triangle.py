# Given a triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

# odd_row(1)  ==  [1]
# odd_row(2)  ==  [3, 5]
# odd_row(3)  ==  [7, 9, 11]
# Note: your code should be optimized to handle big inputs.

def odd_row(n):
    if n == 1:
        return [1]
    else:
        first = sum([i * 2 for i in range(1, n)]) + 1
        last = first + (2 * n)
        return [j for j in range(first, last, 2)]


# def odd_row(n):
#     return list(range(n**2 - n + 1, n**2 + n, 2))