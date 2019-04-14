class Node:
    def __init__(self, key, prev, next):
        self.key = key
        self.prev = prev
        self.next = next
    
class LRUCache: # not tested
    def __init__(self, n):
        self._ll_head = None
        self._ll_tail = None
        self.dict = {}
        self.limit = n 
    
    def set(self, key, value):
        if len(self.dict) >= self.limit:
            self.dict.pop(self._ll_head.key)
            self._ll_head = self._ll_head.next
        self._ll_tail = Node(key, self._ll_tail, None)
        if self._ll_tail.prev is not None:
            self._ll_tail.prev.next = self._ll_tail
        else:
            self._ll_head = self._ll_tail
        self.dict[key] = (value, self._ll_tail)
        
    def get(self, key):
        val, node = self.dict[key]
        if node.prev:
            node.prev.next = node.next 
        if node.next:
            node.next.prev = node.prev 
        self._ll_tail.next = node 
        node.next = None 
        node.prev = self._ll_tail
        return val 
