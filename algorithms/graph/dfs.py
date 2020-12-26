import unittest
#             A
#         ____|____
#         |       |
#         B       C
#     ____|____   |____
#     |       |       |
#     D       E       H
# ____|   ____|       |____
# |       |               |
# F       G               J
# |
# I
#

example_graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "H"],
    "D": ["B", "F"],
    "E": ["B", "G"],
    "F": ["D", "I"],
    "G": ["E"],
    "H": ["C", "J"],
    "I": ["F"],
    "J": ["H"]
}

example_result = ["A", "C", "H", "J", "B", "E", "G", "D", "F", "I"]


def solution(graph: dict, search: str):
    visited = list()
    stack = list()

    stack.append(search)

    while stack:
        search = stack.pop()
        if search not in visited:
            visited.append(search)
            stack.extend(graph.get(search))

    return visited


class DepthFirstSearch(unittest.TestCase):
    def setUp(self) -> None:
        self._graph = example_graph
        self._result = example_result

    def test_solution(self):
        result = solution(graph=self._graph, search="A")
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()