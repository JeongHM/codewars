
def solution(numbers: list, search: int):
    for idx, number in enumerate(numbers):
        if number == search:
            return idx
    return None
