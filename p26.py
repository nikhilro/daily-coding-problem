class Node: 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def remove(self, k):  # remove kth element, O(n) time, O(1) space (tho stack usage)
        def helper(prev, cur, k):
            if cur is None:
                return k
            num = helper(cur, cur.next, k)
            if num == 0:
                if prev is not None:
                    prev.next = cur.next
                del cur
            elif num is None:
                return
            else:
                return num - 1

        helper(None, self, k)

    def remove_2(self, k):  # O(n) time, O(1) space (and no stack overhead)
        leading, lagging_cur, lagging_prev = self, self, None
        for _ in range(k):
            leading = leading.next
        while leading.next is not None:
            leading, lagging_cur, lagging_prev = leading.next, lagging_cur.next, lagging_cur
        if lagging_prev is not None:
            lagging_prev.next = lagging_cur.next
        del lagging_cur
    
    def __str__(self):
        return "{} -> {}".format(self.val, str(self.next))

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
head.remove(3)
print(head)
head.remove_2(2)
print(head)
