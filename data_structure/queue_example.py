

class Queue(object):
    def __init__(self):
        self._queue_list = list()
        self._first_index = 0

    def enqueue(self, obj: object):
        """
        insert queue value
        :param obj: insert ojbect
        :return: None
        """
        queue_size = len(self._queue_list)
        self._queue_list.insert(queue_size, obj)

    def dequeue(self) -> object:
        """
        delete queue vaule
        :return: deleted object
        """
        obj = self._queue_list[self._first_index]
        del self._queue_list[self._first_index]
        return obj

    def __len__(self) -> int:
        """
        get queue length
        :return: queue length
        """
        return len(self._queue_list)


def main():
    my_queue = Queue()
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue("my")
    my_queue.enqueue("name")
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())


if __name__ == '__main__':
    main()