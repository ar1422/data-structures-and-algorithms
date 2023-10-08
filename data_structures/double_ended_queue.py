from queue import Queue
from utility import Node


class DoubleEndedQueue(Queue):

    def enqueue_front(self, node):
        if self.front is None:
            self.enqueue(node)

        else:
            if not isinstance(node, Node):
                node = Node(node)

            node.next = self.front
            self.front = node

    def dequeue_end(self):
        assert not self.is_empty()
        popped_element = self.end.val

        if self.front == self.end:
            self.front = None
            self.end = None
        else:
            temp = self.front
            while temp.next != self.end:
                temp = temp.next
            self.end = temp
            self.end.next = None

        return popped_element


def main():
    de_queue = DoubleEndedQueue()
    de_queue.enqueue(10)
    de_queue.enqueue(15)
    de_queue.enqueue(20)
    de_queue.enqueue(25)
    print(de_queue)
    print("Element popped: " + str(de_queue.dequeue()))
    de_queue.enqueue_front(5)
    print(de_queue)
    print("Element popped: " + str(de_queue.dequeue_end()))
    print(de_queue)
    return None


if __name__ == '__main__':
    main()
