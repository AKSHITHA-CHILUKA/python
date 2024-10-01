class Node:
    """Internal node class to represent data in the linked list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    """Simple linked list implementation to support stack operations."""
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

    def remove_last(self):
        """Remove and return the last element of the linked list."""
        if self._size == 0:
            raise IndexError("remove from empty list")
        
        current = self.head
        if self._size == 1:
            data = current.data
            self.head = self.tail = None
            self._size -= 1
            return data
        
        # Traverse to the second last node
        while current.next != self.tail:
            current = current.next
        data = self.tail.data
        self.tail = current
        self.tail.next = None
        self._size -= 1
        return data

    def peek_last(self):
        """Return the last element without removing it."""
        if self._size == 0:
            raise IndexError("peek from empty list")
        return self.tail.data

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

class Stack:
    """A linked list implementation of a stack."""
    def __init__(self):
        """Create an empty stack."""
        self.list = LinkedList()

    def push(self, elem):
        """Push an element on the stack."""
        self.list.add_last(elem)

    def pop(self):
        """Pop an element off the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.list.remove_last()

    def peek(self):
        """Peek the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.list.peek_last()

    def size(self):
        """Return the number of elements in the stack."""
        return self.list.size()

    def is_empty(self):
        """Check if the stack is empty."""
        return self.list.is_empty()

    def __iter__(self):
        """Allow users to iterate through the stack using an iterator."""
        return iter(self.list)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())  # Output: 3
    print(stack.peek())  # Output: 2
    print(stack.size())  # Output: 2

    for item in stack:
        print(item)  # Output: 2, 1
