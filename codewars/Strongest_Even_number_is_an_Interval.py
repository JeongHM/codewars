import math

def strongest_even(n, m):
    answer_dict = {}
    for i in range(n, m+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
            else:
                continue
        answer_dict.update({i: cnt})
    print(answer_dict)

strongest_even(5, 10)