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
example_result = ["A", "B", "C", "D", "E", "H", "F", "G", "J", "I"]


def solution(graph: dict, search: str or int):
    visited = list()
    queue = list()

    queue.append(search)

    while queue:
        search = queue.pop(0)
        if search not in visited:
            visited.append(search)
            queue.extend(graph.get(search))
    return visited


class BreadthFirstSearch(unittest.TestCase):
    def setUp(self) -> None:
        self._start = "A"
        self._graph = example_graph
        self._result = example_result

    def test_solution(self):
        result = solution(graph=self._graph, search=self._start)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()


