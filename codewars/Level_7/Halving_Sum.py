# Task
# Given a positive integer n, calculate the following sum:

# n + n/2 + n/4 + n/8 + ....
# All elements of the sum are the results of integer division.

# Example
# 25  =>  25 + 12 + 6 + 3 + 1 = 47


# 1. while문 사용 ? 
# 2. n 의 limit을 찾은 후 for 문으로 수를 구한 후 sum 내장 함수 사용 ?

def halving_sum(n): 
    m = 1
    res = list()
    while m <= n:
        res.append(divmod(n, m)[0])
        m *= 2
    return sum(res)



# Other Solution
# import math
# def halving_sum(n): 
#     return sum(n//(2**x) for x in range(int(math.log2(n))+1))

# def halving_sum(n):
#     r = 0
#     while n:
#         r += n
#         n >>= 1
#     return r
