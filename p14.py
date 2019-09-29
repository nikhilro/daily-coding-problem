from random import seed, uniform
from math import pow
import multiprocessing
from multiprocessing import Pool
import time

def pi_monte_carlo(iter = 10000000):
    def helper():
        point = (uniform(-1, 1), uniform(-1, 1))
        return point[0] * point[0] + point[1] * point[1] < 1

    circle_count = 0
    for _ in range(iter):
        circle_count += helper()

    return 4 * circle_count / iter

# print(pi_monte_carlo())

# how to make parallel?
def sample():
    seed(10)
    point = (uniform(-1, 1), uniform(-1, 1))
    return point[0] * point[0] + point[1] * point[1] < 1

# def pi_monte_carlo_parallel(iter = 10000000):
# print(pi_monte_carlo_parallel())

if __name__ == '__main__':
    proc_count = multiprocessing.cpu_count()
    print('You have {} CPUs'.format(proc_count))

    partition_count = [10000000 // proc_count for i in range(proc_count)]

    pool = Pool(processes = proc_count)

    count = pool.map(pi_monte_carlo, partition_count)

    print(4 * sum(count) / 10000000)