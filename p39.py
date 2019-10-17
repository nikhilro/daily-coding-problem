import pprint

# implementation problem, didn't spend much time on it
class ConwayGameOfLife:
    def __init__(self, ticks, coords):
        self.ticks = ticks
        self.board = [[] * max(coords, key=lambda x: x[0])] \
            * max(coords, key=lambda x: x[1])
        for x, y in coords:
            self.board[y][x] = 1 

    def neighbours(self, x, y):
        # write out all the cases
        return 0

    
    def __call__(self):
        for _ in range(self.ticks):
            for y in self.board:
                for x in self.board[y]:
                    neighbours = self.neighbours(x, y)
                    # all game conditions, add columns and rows as needed

            pprint.pprint(self.board)
