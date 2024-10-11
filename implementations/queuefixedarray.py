class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
        self.start = 0

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.full():
            raise Exception("The queue is full")
        self.array[(self.start + self.size) % self.capacity] = value
        self.size +=1
        
    def dequeue(self):
        if self.empty():
            raise Exception("The queue is empty")
        item = self.array[self.start]
        self.array[self.start] = None
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return item

