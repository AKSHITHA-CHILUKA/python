class Node:
    """Internal node class to represent data in the doubly linked list."""
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    """A doubly linked list implementation."""
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clear(self):
        """Empty this linked list, O(n)"""
        trav = self.head
        while trav:
            next_node = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next_node
        self.head = self.tail = None
        self.size = 0

    def __len__(self):
        """Return the size of this linked list."""
        return self.size

    def is_empty(self):
        """Is this linked list empty?"""
        return self.size == 0

    def add(self, elem):
        """Add an element to the tail of the linked list, O(1)"""
        self.add_last(elem)

    def add_last(self, elem):
        """Add a node to the tail of the linked list, O(1)"""
        if self.is_empty():
            self.head = self.tail = Node(elem)
        else:
            self.tail.next = Node(elem, self.tail)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, elem):
        """Add an element to the beginning of this linked list, O(1)"""
        if self.is_empty():
            self.head = self.tail = Node(elem)
        else:
            self.head.prev = Node(elem, None, self.head)
            self.head = self.head.prev
        self.size += 1

    def peek_first(self):
        """Check the value of the first node if it exists, O(1)"""
        if self.is_empty():
            raise RuntimeError("Empty list")
        return self.head.data

    def peek_last(self):
        """Check the value of the last node if it exists, O(1)"""
        if self.is_empty():
            raise RuntimeError("Empty list")
        return self.tail.data

    def remove_first(self):
        """Remove the first value at the head of the linked list, O(1)"""
        if self.is_empty():
            raise RuntimeError("Empty list")

        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None

        return data

    def remove_last(self):
        """Remove the last value at the tail of the linked list, O(1)"""
        if self.is_empty():
            raise RuntimeError("Empty list")

        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1

        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None

        return data

    def remove(self, node):
        """Remove an arbitrary node from the linked list, O(1)"""
        if node.prev is None:  # Removing the head
            return self.remove_first()
        if node.next is None:  # Removing the tail
            return self.remove_last()

        # Bypass the node
        node.next.prev = node.prev
        node.prev.next = node.next

        data = node.data
        node.data = node.prev = node.next = None
        self.size -= 1

        return data

    def remove_at(self, index):
        """Remove a node at a particular index, O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index < self.size // 2:  # Search from the front
            trav = self.head
            for _ in range(index):
                trav = trav.next
        else:  # Search from the back
            trav = self.tail
            for _ in range(self.size - 1, index, -1):
                trav = trav.prev

        return self.remove(trav)

    def remove_value(self, value):
        """Remove a particular value in the linked list, O(n)"""
        trav = self.head

        while trav:
            if trav.data == value:
                self.remove(trav)
                return True
            trav = trav.next

        return False

    def index_of(self, value):
        """Find the index of a particular value in the linked list, O(n)"""
        index = 0
        trav = self.head

        while trav:
            if trav.data == value:
                return index
            trav = trav.next
            index += 1

        return -1

    def contains(self, value):
        """Check if a value is contained within the linked list."""
        return self.index_of(value) != -1

    def __iter__(self):
        """Provide an iterator for the linked list."""
        self.current = self.head
        return self

    def __next__(self):
        """Return the next element in the iteration."""
        if self.current is None:
            raise StopIteration()
        data = self.current.data
        self.current = self.current.next
        return data

    def __str__(self):
        """String representation of the linked list."""
        elements = []
        trav = self.head
        while trav:
            elements.append(repr(trav.data))
            trav = trav.next
        return "[ " + ", ".join(elements) + " ]"
