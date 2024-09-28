class DynamicArray:
    def __init__(self, capacity=16):
        if capacity < 0:
            raise ValueError(f"Illegal Capacity: {capacity}")
        self._capacity = capacity
        self._len = 0
        self._arr = [None] * capacity

    def size(self):
        return self._len

    def is_empty(self):
        return self.size() == 0

    def get(self, index):
        if index < 0 or index >= self._len:
            raise IndexError("Index out of bounds")
        return self._arr[index]

    def set(self, index, elem):
        if index < 0 or index >= self._len:
            raise IndexError("Index out of bounds")
        self._arr[index] = elem

    def clear(self):
        for i in range(self._len):
            self._arr[i] = None
        self._len = 0

    def add(self, elem):
        if self._len >= self._capacity:
            self._resize()
        self._arr[self._len] = elem
        self._len += 1

    def _resize(self):
        new_capacity = self._capacity * 2 if self._capacity > 0 else 1
        new_arr = [None] * new_capacity
        for i in range(self._len):
            new_arr[i] = self._arr[i]
        self._arr = new_arr
        self._capacity = new_capacity

    def remove_at(self, rm_index):
        if rm_index < 0 or rm_index >= self._len:
            raise IndexError("Index out of bounds")
        data = self._arr[rm_index]
        new_arr = [None] * (self._len - 1)
        for i in range(self._len):
            if i < rm_index:
                new_arr[i] = self._arr[i]
            elif i > rm_index:
                new_arr[i - 1] = self._arr[i]
        self._arr = new_arr
        self._capacity -= 1
        self._len -= 1
        return data

    def remove(self, obj):
        index = self.index_of(obj)
        if index == -1:
            return False
        self.remove_at(index)
        return True

    def index_of(self, obj):
        for i in range(self._len):
            if self._arr[i] is None and obj is None:
                return i
            elif self._arr[i] == obj:
                return i
        return -1

    def contains(self, obj):
        return self.index_of(obj) != -1

    def __iter__(self):
        for i in range(self._len):
            yield self._arr[i]

    def __str__(self):
        if self._len == 0:
            return "[]"
        else:
            return "[" + ", ".join(str(self._arr[i]) for i in range(self._len)) + "]"
