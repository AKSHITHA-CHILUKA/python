class IntStack:
    """A quick and lightweight integer-only stack implementation."""
    
    def __init__(self, max_size):
        """Initialize the stack with a maximum size."""
        self.ar = [0] * max_size
        self.pos = 0

    def size(self):
        """Returns the number of elements inside the stack."""
        return self.pos

    def is_empty(self):
        """Returns True if the stack is empty, else False."""
        return self.pos == 0

    def peek(self):
        """Returns the element at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.ar[self.pos - 1]

    def push(self, value):
        """Add an element to the top of the stack."""
        self.ar[self.pos] = value
        self.pos += 1

    def pop(self):
        """Remove and return the element at the top of the stack."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        self.pos -= 1
        return self.ar[self.pos]

    @staticmethod
    def benchmark_test():
        """Benchmark IntStack against Python's built-in list."""
        n = 10000000
        int_stack = IntStack(n)

        # Benchmark IntStack
        import time
        start = time.time()
        for i in range(n):
            int_stack.push(i)
        for i in range(n):
            int_stack.pop()
        end = time.time()
        print(f"IntStack Time: {end - start:.6f} seconds")

        # Benchmark built-in list as stack
        list_stack = []
        start = time.time()
        for i in range(n):
            list_stack.append(i)
        for _ in range(n):
            list_stack.pop()
        end = time.time()
        print(f"List Stack Time: {end - start:.6f} seconds")

# Example usage
if __name__ == "__main__":
    s = IntStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print(s.pop())  # 5
    print(s.pop())  # 4
    print(s.pop())  # 3

    s.push(3)
    s.push(4)
    s.push(5)

    while not s.is_empty():
        print(s.pop())

    IntStack.benchmark_test()
