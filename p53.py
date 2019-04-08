import collections.abc

class NaiveQueue(collections.abc.Iterable, collections.abc.Sized):
    def __init__(self):
        self.s1 = [] # stack 1
        self.s2 = [] # stack 2
        self._len = 0
    
    def __iter__(self):
        return iter(self.s2)

    def __len__(self):
        return self._len

    def enqueue(self, val): # O(n) time
        while self.s2:
            self.s1.append(self.s2.pop())
        self.s2.append(val)
        while self.s1:
            self.s2.append(self.s1.pop())
        self._len += 1
        
    def dequeue(self): # O(1) time
        self._len -= 1
        return self.s2.pop()

class Queue(collections.abc.Sized):
    def __init__(self):
        self.s1 = []
        self.s2 = [] 
        self._len = 0
    
    def __len__(self):
        return self._len
    
    def enqueue(self, val): # O(1) time
        self.s2.append(val)

    def dequeue(self): # amortized O(1) time
        if not self.s1:
            while self.s2:
                self.s1.append(self.s2.pop())
        return self.s1.pop()