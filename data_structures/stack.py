"""
File for implementing the Stack class. This utilizes Node class from utility.py
"""

from utility import Node


class Stack(object):
    """
    Stack class - Follows LIFO methodology
    """

    def __init__(self):
        self.top = None

    def is_empty(self):
        """
        Function to check if the Stack is empty.
        :return: Boolean indicating whether the stack is empty.
        """

        return self.top is None

    def push(self, node):
        """
        Insert/Push an element into the stack.
        :param node: Node/Value that needs to be inserted.
        :return: None
        """

        if not isinstance(node, Node):
            node = Node(node)

        node.next = self.top
        self.top = node

    def pop(self):
        """
        Function remove the last inserted element. The function raises AssertionError if the stack is empty.
        :return: The removed element.
        """
        assert not self.is_empty()

        pop_element = self.top.val
        self.top = self.top.next
        return pop_element

    def __str__(self):
        if self.top is None:
            return ""

        return str(self.top)


def main():
    stack = Stack()
    stack.push(10)
    stack.push(15)
    stack.push(20)
    print(stack)
    print("Element popped: " + str(stack.pop()))
    print("Element popped: " + str(stack.pop()))
    print(stack)
    print("Element popped: " + str(stack.pop()))
    print(stack)


if __name__ == '__main__':
    main()
