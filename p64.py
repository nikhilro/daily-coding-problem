def num_knight_tours(n):
    moves = set()
    def helper(i, j):
        if 0 > i or i > n - 1 or 0 > j or j > n - 1:
            return 0 
        if len(moves) == n * n:
            return 1
        count = 0
        for x, y in [(2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (-1, 2)]:
            if (i + x, j + y) not in moves:
                moves.add((i + x, j + y))
                count += helper(i + x, j + y)
                moves.remove((i + x, j + y))
        return count

    def initializer_helper():
        count = 0
        for i in range(n):
            for j in range(n):
                moves.add((i, j))
                count += helper(0, 0)
                moves.remove((i, j))
        return count
    
    return initializer_helper()