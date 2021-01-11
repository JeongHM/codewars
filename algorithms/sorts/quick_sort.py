import random
import unittest


def solution(numbers: list):
    if len(numbers) <= 1:
        return numbers

    left = list()
    right = list()
    pivot = numbers[0]

    for idx in range(1, len(numbers)):
        if numbers[idx] < pivot:
            left.append(numbers[idx])
        else:
            right.append(numbers[idx])

    return solution(left) + [pivot] + solution(right)


def solution2(numbers: list):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    left = solution2([numbers[idx] for idx in range(1, len(numbers)) if numbers[idx] < pivot])
    right = solution2([numbers[idx] for idx in range(1, len(numbers)) if pivot <= numbers[idx]])

    return left + [pivot] + right


class QuickSortTest(unittest.TestCase):
    def setUp(self) -> None:
        self._random_numbers = random.sample(range(1000), 20)

    def test_quick_sort(self):
        quick_sort = solution(self._random_numbers)
        self.assertEqual(sorted(self._random_numbers), quick_sort)

    def test_quick_sort_2(self):
        quick_sort = solution2(self._random_numbers)
        self.assertEqual(sorted(self._random_numbers), quick_sort)

if __name__ == '__main__':
    unittest.main()