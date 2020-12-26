# 무작위 숫자가 들어있는 리스트(numbers) 에서 검색하고자하는 숫자 (search) 값의 유무를 리턴
import random
import unittest


def solution(numbers: list, search: int):
    if not isinstance(numbers, list) or not isinstance(search, int):
        raise TypeError("numbers must be list, search must be int")

    if len(numbers) == 0 or (len(numbers) == 1 and numbers[0] != search):
        return False
    if len(numbers) == 1 and numbers[1] == search:
        return True

    numbers = sorted(numbers)
    median = len(numbers) // 2

    if search == numbers[median]:
        return True

    if search < numbers[median]:
        return solution(numbers=numbers[:median], search=search)
    return solution(numbers=numbers[median + 1:], search=search)


class BinarySearchTest(unittest.TestCase):
    def setUp(self) -> None:
        self._search = 20
        self._numbers = random.sample(range(1000), 20)
        self._invalid_type_numbers = (i for i in self._numbers)
        self._invalid_type_search = "a"

    def test_binary_search_with_numbers(self):
        """
        test with random numbers
        :return: None
        """
        result = solution(numbers=self._numbers, search=self._search)
        self.assertEqual(self._search in self._numbers, result)

    def test_binary_search_with_invalid_numbers_type(self):
        """
        test numbers type error
        :return: None
        """
        self.assertRaises(TypeError, solution, self._invalid_type_numbers, self._search)

    def test_binary_search_with_invalid_search_type(self):
        """
        test numbers type error
        :return: None
        """
        self.assertRaises(TypeError, solution, self._numbers, self._invalid_type_search)


if __name__ == '__main__':
    unittest.main()
