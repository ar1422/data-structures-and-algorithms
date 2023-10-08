"""
File for implementing the Queue class. This utilizes Node class from utility.py
"""
from utility import Node


class Queue(object):

    def __init__(self):
        self.front = None
        self.end = None

    def is_empty(self):
        return self.front is None and self.end is None

    def enqueue(self, node):

        if not isinstance(node, Node):
            node = Node(node)

        if self.front is None:
            self.front = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def dequeue(self):

        assert not self.is_empty()
        popped_element = self.front.val
        self.front = self.front.next
        if self.front is None:
            self.end = None

        return popped_element

    def __str__(self):
        if self.front is None:
            return ""

        return str(self.front)


def main():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    print(queue)
    print("Element popped: " + str(queue.dequeue()))
    print("Element popped: " + str(queue.dequeue()))
    print(queue)
    print("Element popped: " + str(queue.dequeue()))
    print(queue)


if __name__ == '__main__':
    main()
