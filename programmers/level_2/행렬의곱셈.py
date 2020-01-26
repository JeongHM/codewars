# 행렬의 곱셈
# 문제 설명
# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다.
# 입출력 예
# arr1	arr2	return
# [[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
# [[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]


def solution(arr1, arr2):
    arr2 = reverse(arr=arr2)
    list1 = list()
    for ar2 in arr2:
        list2 = list()
        for ar1 in arr1:
            list3 = list()
            for n, a1 in enumerate(ar1):
                list3.append(ar2[n] * a1)
            list2.append(sum(list3))
        list1.append(list2)
    return reverse(arr=list1)


def reverse(arr):
    arr_length = len(arr[0])
    return_dict = {n: list() for n in range(arr_length + 1)}
    for ar in arr:
        for n, a in enumerate(ar):
            return_dict[n].append(a)
    return [value for key, value in return_dict.items() if value]


# 다른사람 풀이 1
# zip(*array) = 행과 열을 바꿔주는 역확을 함

def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


# 다른사람 풀이 2
## np.matrix([[1, 2], [3, 4]])
# matrix([[1, 2],
# [3, 4]]

# import numpy as np
# def productMatrix(A, B):
#     return (np.matrix(A)*np.matrix(B)).tolist()
