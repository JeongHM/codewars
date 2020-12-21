def solution(numbers: list):
    numbers_length = len(numbers)
    for index in range(numbers_length - 1):
        swap = True
        for idx in range(numbers_length - index - 1):
            if numbers[idx] > numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
            else:
                swap = False
        if swap is False:
            break
    return numbers

