# Program the function distance(p1, p2) which returns the distance between the points p1 and p2 in n-dimensional space.
# p1 and p2 will be given as arrays.


# Your program should work for all lengths of arrays, and should return -1 if the arrays aren't of the same length or if both arrays are empty sets.


# If you don't know how to measure the distance between two points, go here:

def distance(p1, p2):
    if not p1 or not p2 or (len(p1) != len(p2)):
        return -1
    
    answer = [(_p1 - _p2) ** 2 for _p1, _p2 in zip(p1, p2)]
    return sum(answer) ** 0.5




# Other Answer 
# def distance(p1, p2):
#     from functools import reduce
#     from math import hypot
#     if not p1 or len(p1) != len(p2): return -1
#     return reduce(hypot, (x-y for x,y in zip(p1, p2)))

# def distance(p1, p2):
#     return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5 if len(p1) == len(p2) > 0 else -1