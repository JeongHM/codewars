# double linked list
# 이중 연결 리스트라고 하며, 양방향으로 연결되어 있어 어디든 탐색  가


class Node(object):
    def __init__(self, data: object, prev_address: object = None, next_address: object = None):
        self._data = data
        self._prev_address = prev_address
        self._next_address = next_address


class NodeController(object):
    def __init__(self, data: object):
        self._head = Node(data=data)
        self._tail = self._head

    def add_node(self, data: object):
        if self._head is None:
            self._head = Node(data=data)
            self._tail = self._head
        else:
            node = self._head
            while node._next_address:
                node = node._next_address

            new_node = Node(data=data)
            node._next_address = new_node
            new_node._prev_address = node
            self._tail = new_node

    def before_add_node(self, data: object, before_node_data: object):
        if self._head is None:
            self._head = data
            return True

        node = self._tail
        while node._data != before_node_data:
            node = node._prev_address

            if node is None:
                return False

        new_node = Node(data=data)
        before_new_node = node._prev_address
        before_new_node._next_address = new_node

        new_node._prev_address = before_new_node
        new_node._next_address = node

        node._prev_address = new_node
        return True

    def get_all_nodes(self):
        node = self._head
        while node:
            print(node._prev_address, node._data, node._next_address)
            node = node._next_address

    def search_from_head(self, data):
        """
        :param data: search data
        :return: if data is exist: node, else false
        """
        node = self._head
        while node:
            if node._data == data:
                return node
            node = node._next_address
        return False

    def search_from_tail(self, data):
        """
        search from tail
        :param data: search data
        :return: if data is exist: node, else false
        """
        node = self._tail
        while node:
            if node._data == data:
                return node
            node = node._prev_address
        return False


def test_add_node():
    double_linked_list = NodeController(data=0)
    for data in range(1, 10):
        double_linked_list.add_node(data=data)

    double_linked_list.add_node(10)
    double_linked_list.get_all_nodes()


def test_add_before_node():
    double_linked_list = NodeController(data=1)
    for data in range(2, 10):
        double_linked_list.add_node(data=data)

    double_linked_list.before_add_node(data=1.5, before_node_data=2)
    double_linked_list.get_all_nodes()


if __name__ == '__main__':
    test_add_before_node()
