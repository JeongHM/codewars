# Description
# The task is described in the title: find the sum of all numbers with the same digits(permutations) including duplicates. However, due to the fact that this is a performance edition kata, num can go up to 10**10000. That's a number with 10001 digits(at most). Be sure to use efficient algorithms and good luck! All numbers tested for will be positive.

# Examples

# sum_arrangements(123) returns 1332 #123 + 132 + 213 + 231 + 312 + 321 = 1332
# sum_arrangements(1185) returns 99990 #1185 + 1158 + 1815 + 1851 + 1518 + 1581 + 1185 + 1158 + 1815 + 1851 + 1518 + 1581 + 8115 + 8151 + 8115 + 8151 + 8511 + 8511 + 5118 + 5181 + 5118 + 5181 + 5811 + 5811 = 99990
from itertools import permutations

def sum_arrangements(num):
    generator_num = 
    answer = map(int, map(''.join, permutations(iterable=iter_num)))
    return sum(answer)
    

sum_arrangements(123)


# from math import factorial

# def sum_arrangements(num):

#     snum = str(num)
#     leng = len(snum)
#     total = 0
#     c = factorial(leng - 1) * sum(map(int, snum))

#     for i in range(leng):
#         total += c
#         c *= 10

#     return total



# def sum_arrangements(num):
#     num = str(num)
#     n = 1
#     number = len(num)
#     for i in range(1,number):
#         n *= i
#     return int('1'*number)*sum(int(i) for i in num)*n



# def factorial(n):
#     res = 1
#     for i in range(1,n+1):
#         res *= i
#     return res
# def sum_arrangements(num):
#     #your code here
#     #print(num)
#     s = str(num)
#     n = len(s)
#     fac = 0
#     for _ in range(n):
#         fac *= 10
#         fac += 1
#     digitSum = sum([int(i) for i in s])
#     return digitSum * fac * factorial(n-1)