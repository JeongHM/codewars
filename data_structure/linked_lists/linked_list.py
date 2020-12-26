
class Node(object):
    def __init__(self, data: object, next_address=None):
        self._data = data
        self._next_address = next_address


class NodeController(object):
    def __init__(self, data):
        self._head = Node(data)

    def add_node(self, data):
        if self._head is None:
            self._head = Node(data)
        else:
            node = self._head
            while node._next_address:
                node = node._next_address
            node._next_address = Node(data)

    def delete_node(self, data: object):
        if self._head is None:
            return

        if self._head._data == data:
            temp = self._head
            self._head = self._head._next_address
            del temp
            return

        else:
            node = self._head
            while node._next_address:
                if node._next_address._data == data:
                    temp = node._next_address
                    node._next_address = node._next_address._next_address
                    del temp
                else:
                    node = node._next_address

    def search_node(self, data: object):
        if self._head is None:
            return

        node = self._head

        while node:
            if node._data == data:
                print(f"search data : {node._data}")
                return
            node = node._next_address

    def get_all_nodes(self):
        node = self._head
        while node:
            print(node._data, node._next_address)
            node = node._next_address

def test_search_node():
    search_node = 4

    linked_list = NodeController(data=0)
    for data in range(1, 10):
        linked_list.add_node(data=data)
    linked_list.search_node(data=search_node)


def test_delete_header_node():
    linked_list = NodeController(data=1)
    assert linked_list._head._data == 1

    linked_list.delete_node(1)
    assert linked_list._head is None


def test_delete_interim_node():
    linked_list = NodeController(data=0)

    for data in range(1, 10):
        linked_list.add_node(data=data)

    linked_list.delete_node(data=4)
    linked_list.get_all_nodes()


def test_add_node():
    linked_list = NodeController(1)
    for data in range(2, 10):
        linked_list.add_node(data=data)
    linked_list.get_all_nodes()


def main():
    linked_list = NodeController(10)
    linked_list.get_all_nodes()


if __name__ == '__main__':
    test_delete_header_node()
    test_delete_interim_node()
    test_search_node()
