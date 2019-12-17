# Given an array, find the integer that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    answer = {i: seq.count(i) for i in set(seq)}
    for key, value in answer.items():
        if value % 2 != 0:
            return key


find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
