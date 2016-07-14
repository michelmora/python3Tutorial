class Stack:
    """Storage and handle a list of elements type Stack(first in first out)."""

    def __init__(self, items=None):
        """Initialize the Stack with None or an initial list of elements.

        stack() -> new empty stack
        stack(iterable) -> new stack initialized from iterable's items(objects)

        Args:
            [items] list of elements(objects) or None for an empty list

        Attributes:
            items (list): The list of elements(the Stack of elements)
        """
        self.items = [] if not items else items

    def is_empty(self):
        """Return if the list is empty or not.

        Return:
            True if the list has no items, False otherwise.

        """
        return self.items == []

    def push(self, item):
        """Add an element at the end of the list.

        Args:
            item: object to be added at the end of the list.

        Return:
            None.

        """
        self.items.append(item)

    def pop(self):
        """Get and remove the last element(object) of the list.

        Return:
            The last element of the list or None if the list is empty.
            Check if not self.is_empty() before use this method
        """
        return self.items.pop()

    def peek(self):
        """Get the last element(object) of the list.

        Return:
            The last element of the list or None if the list is empty.
            Check if not self.is_empty() before use this method
        """
        return self.items[len(self.items) - 1] # if not self.is_empty() else None

    def size(self):
        """Get the len of the list.

        Return:
            Return the len of the list.

        """
        return len(self.items)

    def extend(self, items):
        """Add a list of element at the end of the list.

        Args:
            [items] list of elements(objects) or None for an empty list

        Return:
            None.

        """
        self.items.extend(items)

a = Stack()
b = Stack(['a', 'b', 'c', 'd'])
from collections import deque
d = deque()
print('test')