"""
File to include basic classes definition like Node etc.
Author: Arya Girisha Rao (ar1422@rit.edu)
"""


class Node(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def get_value(self):
        return self.val

    def get_next(self):
        return self.next

    def __str__(self):
        if self.next is None:
            return str(self.val)

        return str(self.val) + " -> " + str(self.next)
