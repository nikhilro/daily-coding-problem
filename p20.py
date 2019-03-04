class Node:
    def __init__(self, val, node = None):
        self.val = val
        self.next = node

    def __str__(self):
        return "{} => {}".format(self.val, str(self.next))

    def reversed(self):
        if not self.next:
            yield self.val 
        else:
            yield from self.next.reversed()
            yield self.val
            
        # works
        # if not self.next:
        #     yield self.val
        # else:
        #     for node in self.next.reversed():
        #         yield node
        #     yield self.val

        # wrong
        # if not self.next:
        #     yield self.val 
        # else: 
        #     self.next.reversed() 
        #     yield self.val

    def intersect(self, other):
        prev_val = None

        try:
            for self_val, other_val in zip(self.reversed(), other.reversed()):
                if self_val != other_val:
                    return prev_val
                else:
                    prev_val = self_val
        except StopIteration:
            return prev_val
            # raise ValueError("Linked Lists {} and {} don't intersect".format(self, other))
    
    def __len__(self):
        if not self.next:
            return 1
        else:
            return 1 + len(self.next) 
        
    def intersect_without_reverse(self, other):
        self_len, other_len = len(self), len(other)

        current_self, current_other = self, other 

        if self_len > other_len:
            for _ in range(self_len - other_len):
                current_self = current_self.next
        else:
            for _ in range(other_len - self_len):
                current_other = current_other.next
        
        while current_other.val != current_self.val:
            current_other, current_self = current_other.next, current_self.next
        
        return current_other.val

# sanity check
root = Node(1, Node(2, Node(3)))
print(root)
print(list(root.reversed()))

l1 = Node(3, Node(7, Node(8, Node(10))))
l2 = Node(99, Node(1, Node(8, Node(10))))

print(l1.intersect(l2))
print(l1.intersect_without_reverse(l2))