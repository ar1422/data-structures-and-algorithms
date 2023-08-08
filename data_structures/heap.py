"""
Description:
The (binary) heap data structure is an array object that we can view as a nearly complete binary tree.
Each node of the tree corresponds to an element of the array.
The tree is completely filled on all levels except possibly the lowest, which is filled from the left up to a point.
There are two kinds of binary heaps: max-heaps and min-heaps.
In both kinds, the values in the nodes satisfy a heap property, the specifics of which depend on the kind of heap.
In a max-heap, the max-heap property is that Parent's value will be greater than or equal to the kids' values.
In a min-heap, the min-heap property is that Parent's value will be lesser than or equal to the kids' values.
"""


def perform_heap_operations(elements):
    """
    Function to demonstrate heap operations
    :param elements: The list of elements to work with
    :return: None
    """
    elements_copy = elements.copy()
    import heapq

    # To heapify a given list of elements, we can use heapq.heapify(list) function.

    heapq.heapify(elements_copy)

    # To remove any elements from the heap, we can use the heapq.heappop(heap) function.
    ascending_order = [heapq.heappop(elements_copy) for _ in range(len(elements))]
    print(ascending_order)
    # To add any element to the heap, we can use the heapq.heappush(heap,element) function.

    heapq.heappush(elements, 100)

    elements_reverse = [-1 * x for x in elements]
    heapq.heapify(elements_reverse)
    descending_order = [heapq.heappop(elements_reverse) * -1 for _ in range(len(elements_reverse))]
    print(descending_order)


def main():
    elements = [10, 5, 30, 25, 40, 20, 15]
    perform_heap_operations(elements)


if __name__ == '__main__':
    main()
