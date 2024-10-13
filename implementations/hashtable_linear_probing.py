class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.count = 0

    def hash(self, key):
        return hash(key) % self.capacity

    def add(self, key, value):
        index = self.hash(key)
        init_index = index

        while self.table[index][0] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity
            if index == init_index:
                raise Exception("Hash table is full")

            self.table[index] = (key, value)
            self.count += 1

    def exists(self, key):
        index = self.hash(key)
        init_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.capacity
            if index == init_index:
                break

    def get(self, key):
        index = self.hash(key)
        initial_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
            if index == initial_index:  # Full loop
                break

        raise KeyError(f"Key {key} not found")

    def remove(self, key):
        index = self.hash(key)
        init_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] == None
                self.count -= 1
                self.rehash_from(index)
                return
            index = (index + 1) % self.capacity
            if index == init_index:
                break

    def rehash_from(self, index):
        next_index = (index + 1) % self.capacity
        while self.table[next_index] is not None:
            key, value = self.table[next_index]
            self.table[next_index] = None
            self.count -= 1
            self.add(key, value)
            next_index = (next_index + 1) % self.capacity
