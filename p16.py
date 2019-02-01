class Deque: 
    # based on circular vector / ring buffer / circular buffer
    def __init__(self, n):
        self.lst = [0] * n
        self.index = n - 1

    def record(self, order_id):
        if self.index >= len(self.lst) - 1:
            self.index = 0
        else:
            self.index += 1

        self.lst[self.index] = order_id

        return

    def get_last(self, i):
        return self.lst[self.index - i]


class Deque2:
    # more pythonic naming

    def __init__(self, n):
        self._log = [0] * n
        self._cur = n - 1

    def record(self, order_id):
        self._cur = (self._cur + 1) % len(self._log)
        self._log[self._cur] = order_id

    def get_last(self, i):
        return self._log[self._cur - i]
