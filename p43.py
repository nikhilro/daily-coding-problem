class Stack:
    def __init__(self):
        self._data = []
        self._max = []
    
    def push(self, val):
        self._data.append(val)
        if not self._max or val > self._max[-1]: # could also keep 1-to-1 tracking with max(val, self._max[-1])
            self._max.append(len(self._data) - 1)
    
    def pop(self):
        if self._max[-1] == len(self._data) - 1:
            self._max.pop()
        return self._data.pop()
    
    def max(self):
        return self._data[self._max[-1]]
