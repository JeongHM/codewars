import random
import unittest


def solution(numbers: list):
    numbers_length = len(numbers)
    for index in range(numbers_length):
        min_index = index
        for idx in range(index + 1, numbers_length):
            if numbers[min_index] > numbers[idx]:
                min_index = idx
        numbers[index], numbers[min_index] = numbers[min_index], numbers[index]
    return numbers


class SelectionSortTest(unittest.TestCase):
    def setUp(self) -> None:
        self._random_numbers = random.sample(range(1000), 20)

    def test_selection_sort(self):
        selection_sort = solution(self._random_numbers)
        self.assertEqual(sorted(self._random_numbers), selection_sort)


if __name__ == '__main__':
    unittest.main()

