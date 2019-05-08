def colorable(graph, k): # not tested, O(n * k * n / k) time, O(n * k) space
    mem = [set() for _ in range(len(graph))]
    for i in range(len(graph)):
        for col in range(k):
            if col not in mem[i]:
                for node, adj in enumerate(graph[i]):
                    if node != i and adj:
                        mem[node].add(col)
            elif col == k - 1:
                return False
    return True
