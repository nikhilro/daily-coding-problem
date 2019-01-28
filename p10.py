import time
import threading


def scheduler_naive(f, n):
    time.sleep(n / 1000)
    f()


start = time.time()
scheduler_naive(lambda: print("hello"), 2000)
print("Duration ", time.time() - start)


class Scheduler_naive:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_call():
            time.sleep(n / 1000)
            f()

        t = threading.Thread(target=sleep_call)
        t.start()


class Scheduler:
    def __init__(self):
        self.funcs = []
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time.time() * 1000
            for func, delay in self.funcs:
                if now > delay:
                    func()
            self.funcs = \
                [(func, delay) for (func, delay) in self.funcs if delay > now]
            time.sleep(0.05)

    def delay(self, f, n):
        self.funcs.append((f, time.time() * 1000 + n))
