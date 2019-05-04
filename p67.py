class Node:
    def __init__(self, key, val, prev, next):
        self.prev = prev
        self.key = key
        self._val = val
        self.next = next
        self.count = 0
    
    @property
    def val(self):
        self.count += 1
        return self._val
    

class LFUCache: # not tested
    def __init__(self, n):
        self.freqs = []
        self.limit = n 
        self.dict = {}
    
    def set(self, key, value):
        if len(self.dict) >= self.limit:
            lowest_freq = 0 
            while self.freqs[lowest_freq] is None:
                lowest_freq += 1
            ll_head, ll_tail = self.freqs[lowest_freq]
            if ll_tail.prev is None: 
                self.freqs[lowest_freq] = None 
            else: 
                self.freqs[lowest_freq] = (ll_head, ll_tail.prev)
                ll_tail.next = None 
            del self.dict[ll_tail.key]
        if not self.freqs:
            ll_head = ll_tail = None
        else: 
            ll_head, ll_head = self.freqs[0]
        self.dict[key] = Node(key, value, ll_tail, None)
        if ll_tail:
            ll_tail.next = self.dict[key]
        if ll_head:
            self.freqs[0] = (ll_head, self.dict[key])
        else:
            self.freqs[0] = (self.dict[key], self.dict[key])
        
    def get(self, key):
        node = self.dict[key]
        if self.freqs[node.count][0] is node:
            self.freqs[node.count] = None 
        val = node.val
        if node.prev:
            node.prev.next = node.next 
            node.prev = None 
        if node.next:
            node.next.prev = node.prev 
            node.next = None 
        if self.freqs[node.count] is not None:
            ll_head, ll_tail = self.freqs[node.count]
            ll_tail.next = node 
            node.prev = self.ll_tail
            self.freqs[node.count] = (ll_head, ll_tail)
        else:
            self.freqs[node.count] = (node, node)
        return val 
