from collections import deque

def deepest_node(root): # O(n) since it visits all nodes, O(n) space to perform dfs
    queue, cur = deque(), root
    while queue:
        queue.extend([cur.left,cur.right])
        nxt = queue.popleft()
        while nxt is None and queue:
            nxt = queue.popleft()
        cur = nxt or cur
    return cur

# could also do bfs