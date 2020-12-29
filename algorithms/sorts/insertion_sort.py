import random
import unittest


def solution(numbers: list):
    numbers_length = len(numbers)
    for index in range(numbers_length - 1):
        for idx in range(index + 1, 0, -1):
            if numbers[idx] < numbers[idx - 1]:
                numbers[idx], numbers[idx - 1] = numbers[idx - 1], numbers[idx]
            else:
                break
    return numbers


class InsertionSortTest(unittest.TestCase):
    def setUp(self) -> None:
        self._random_numbers = random.sample(range(1000), 20)

    def test_insertion_sort(self):
        insertion_sort = solution(self._random_numbers)
        self.assertEqual(sorted(self._random_numbers), insertion_sort)


if __name__ == '__main__':
    unittest.main()