class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.sz = 0

    def size(self):
        return self.sz

    def empty(self):
        if self.sz == 0:
            return True
        return False
    
    def value_at(self, index: int):
        current = self.head.next 
        i = 0
        while current:
            if i == index:
                return current.item
            i += 1
            current = current.next
        raise Exception("index out of bounds")

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head.next 
        self.head.next = new_node
        if not new_node.next:
            # if linked list was empty before inserting
            self.tail = new_node
        self.sz += 1

    def pop_front(self):
        current = self.head
        if not current.next:
            raise Exception("LinkedList is empty")
        value = current.next.item
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next
        return value

    def push_back(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.sz += 1

    def pop_back(self):
        i = 0
        current = self.head
        while i < self.sz and current:
            i += 1
            current = current.next
        value = self.tail.item
        current.next = None
        self.tail = current
        return value
    
    def front(self):
        return self.head.item

    def back(self):
        return self.tail.item

    def insert(self,index,item):
        i = 0
        current = self.head
        while i<index and current:
            i+=1
            current = current.next
        if current and current.next:
            new_node = Node(item)
            new_node.next = current.next
            current.next = new_node
        else:
            raise Exception("Index out of bounds")

    def erase(self, index):
        i = 0
        current = self.head
        while i < index and current:
            i+=1
            current = current.next
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return
        raise Exception("Index out of bounds")
    
    def value_n_from_end(self,n):
        current = self.head.next 
        i = 0
        while current:
            if i == self.sz - n:
                return current.item
            i += 1
            current = current.next
        raise Exception("index out of bounds")

    def remove_value(self,item):
        current = self.head
        i = 0
        while current.item != item:
            i +=1
            current = current.next
        if i > self.sz:
            raise Exception("Not found")
        else:
            self.erase(i)
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            

