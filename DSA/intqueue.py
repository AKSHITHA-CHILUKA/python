class IntQueue:
    """A quick and lightweight integer-only queue implementation."""
    
    def __init__(self, max_size):
        """Initialize the queue with a maximum size."""
        self.size_limit = max_size + 1  # To distinguish full from empty
        self.queue = [0] * self.size_limit
        self.front = 0
        self.end = 0

    def is_empty(self):
        """Return True if the queue is empty, else False."""
        return self.front == self.end

    def size(self):
        """Return the number of elements inside the queue."""
        if self.front > self.end:
            return (self.end + self.size_limit - self.front)
        return self.end - self.front

    def peek(self):
        """Return the front element of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[self.front]

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        if (self.end + 1) % self.size_limit == self.front:
            raise RuntimeError("Queue too small!")
        self.queue[self.end] = value
        self.end = (self.end + 1) % self.size_limit

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        ret_val = self.queue[self.front]
        self.front = (self.front + 1) % self.size_limit
        return ret_val

    @staticmethod
    def benchmark_test():
        """Benchmark IntQueue against Python's built-in list as a queue."""
        import time

        n = 10000000
        int_queue = IntQueue(n)

        # Benchmark IntQueue
        start = time.time()
        for i in range(n):
            int_queue.enqueue(i)
        for _ in range(n):
            int_queue.dequeue()
        end = time.time()
        print(f"IntQueue Time: {end - start:.6f} seconds")

        # Benchmark Python's built-in list as a queue
        list_queue = []
        start = time.time()
        for i in range(n):
            list_queue.append(i)
        for _ in range(n):
            list_queue.pop(0)  # This is O(n), hence slower
        end = time.time()
        print(f"List Queue Time: {end - start:.6f} seconds")

# Example usage
if __name__ == "__main__":
    q = IntQueue(5)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
    print(q.dequeue())  # Output: 3
    print(q.dequeue())  # Output: 4

    print(q.is_empty())  # Output: False

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())  # Output: 5
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
    print(q.dequeue())  # Output: 3

    print(q.is_empty())  # Output: True

    IntQueue.benchmark_test()
