class Node:
    """Internal node class to represent data in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Simple linked list implementation to support queue operations."""
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add_last(self, data):
        """Add an element to the end of the linked list."""
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._size += 1

    def remove_first(self):
        """Remove and return the first element of the linked list."""
        if self._size == 0:
            raise IndexError("remove from empty list")
        
        data = self.head.data
        self.head = self.head.next
        if self.head is None:  # If the list becomes empty
            self.tail = None
        self._size -= 1
        return data

    def peek_first(self):
        """Return the first element without removing it."""
        if self._size == 0:
            raise IndexError("peek from empty list")
        return self.head.data

    def size(self):
        """Return the size of the linked list."""
        return self._size

    def is_empty(self):
        """Check if the linked list is empty."""
        return self._size == 0

    def __iter__(self):
        """Provide an iterator for the linked list."""
        current = self.head
        while current:
            yield current.data
            current = current.next

class Queue:
    """A simple queue implementation using a linked list."""
    def __init__(self):
        """Create an empty queue."""
        self.list = LinkedList()

    def offer(self, elem):
        """Add an element to the back of the queue."""
        self.list.add_last(elem)

    def poll(self):
        """Remove and return the front element of the queue."""
        return self.list.remove_first()

    def peek(self):
        """Return the front element of the queue without removing it."""
        return self.list.peek_first()

    def size(self):
        """Return the number of elements in the queue."""
        return self.list.size()

    def is_empty(self):
        """Check if the queue is empty."""
        return self.list.is_empty()

    def __iter__(self):
        """Allow users to iterate through the queue using an iterator."""
        return iter(self.list)

# Example usage
if __name__ == "__main__":
    q = Queue()
    q.offer(1)
    q.offer(2)
    q.offer(3)

    print(q.poll())  # Output: 1
    print(q.poll())  # Output: 2
    print(q.peek())  # Output: 3
    print(q.size())  # Output: 1
    print(q.is_empty())  # Output: False

    for item in q:
        print(item)  # Output: 3
