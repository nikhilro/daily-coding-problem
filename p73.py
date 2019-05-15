def reverse(head):
    prev, cur = None, head
    while cur:
        prev, cur, cur.next = cur, cur.next, prev
    