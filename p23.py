import math

steps = {}
path = set()


def min_steps(board, start, end): # dfs, O(m * n) time, O(m * n) space
    def validate(move):
        if move[0] < len(board) and move[0] >= 0 and \
                move[1] < len(board[0]) and move[1] >= 0 and \
                not board[move[0]][move[1]] and \
                move not in path:  # not a wall or prev position
            return 1 + min_steps(board, move, end)
        return math.inf

    if start == end:
        return 0

    if start in steps:
        return steps[start]
    
    path.add(start)
    right = validate((start[0], start[1] + 1))  # right
    down = validate((start[0] + 1, start[1]))  # down
    left = validate((start[0], start[1] - 1))  # left
    up = validate((start[0] - 1, start[1]))  # up
    path.remove(start)

    steps[start] = min(right, down, left, up)

    return steps[start]


board = [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]]

print(min_steps(board, (3, 0), (0, 0)))
