import math
import queue

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

def min_steps_2(board, start, end): # bfs, O(m * n) time, O(m * n) space
    cache = set()
    q = queue.Queue()
    q.put((start, 0))

    def validate(move, steps):
        if move[0] < len(board) and move[0] >= 0 and \
                move[1] < len(board[0]) and move[1] >= 0 and \
                not board[move[0]][move[1]] and \
                move not in cache:  # not a wall or prev position
            return q.put((move, steps + 1))
        
    while not q.empty():
        start, steps = q.get(block=False)
        cache.add(start)

        if start == end:
            return steps
        
        validate((start[0], start[1] + 1), steps)  # right
        validate((start[0] + 1, start[1]), steps)  # down
        validate((start[0], start[1] - 1), steps)  # left
        validate((start[0] - 1, start[1]), steps)  # up

    return None 

print(min_steps_2(board, (3, 0), (0, 0)))



        


