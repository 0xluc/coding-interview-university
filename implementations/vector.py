class Vector:
    def __init__(self, cpcty: int):
        self.cpcty = 16
        while cpcty > self.cpcty:
            self.cpcty *= 2
        self.s = 0
        self.arr = [None] * cpcty

    def __resize(self, new_capacity: int):
        self.cpcty = new_capacity
        new_arr = [None] * self.cpcty

        for i in range(self.s):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def size(self):
        return self.s

    def at(self, index: int):
        if index> self.s:
            raise Exception("Index out of bounds")
        return self.arr[index]

    def insert(self, index: int, item) -> None:
        if self.s == self.capacity:
            self.__resize(self.cpcty * 2)
        if index > self.s:
            raise Exception("Index out of bounds")
        for i in range(index, self.s):
            self.arr[i + 1] = self.arr[i]
        self.arr[index] = item

    def prepend(self, item):
        self.insert(0, item)

    def push(self, value) -> None:
        if self.s == self.capacity:
            self.__resize(self.cpcty * 2)
        self.arr[self.s] = value
        self.s += 1
    
    def pop(self):
        if self.s == 0:
            raise Exception("Error: empty array")
        value = self.arr[self.s]
        self.arr[self.s] = None
        self.s -= 1
        return value
    
    def delete(self, index: int):
        if self.s < self.cpcty // 4:
            self.__resize(self.cpcty // 2)
        if index > self.s:
            raise Exception("Index out of bounds")
        for i in range(index, self.s):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.s] = None
        self.s -= 1
    def remove(self, item):
        """Author wrote: remove(item) - looks for value and removes index holding it (even if in multiple places)
            But I don't quite understand what he mean by it since it's a O(n) operation and deleting all the x elements would mean O(kn)"""
        for i in range(self.s - 1):
            if self.arr[i] == item:
                self.arr[i] = None

    def capacity(self):
        return self.cpcty
    
    def is_empty(self):
        if self.s == 0:
            return True
        return False
    

