import random

def rejection_sampling(n, excluded_nums):
    num = random.randint(0, n - 1)
    while num in excluded_nums:
        num = random.randint(0, n - 1)
    return num

print(rejection_sampling(4, set([0, 3])))

def pre_processing(n, excluded_nums):
    nums = set([i for i in range(n) if i not in excluded_nums])
    return random.sample(nums, 1)[0]

print(pre_processing(4, set([0, 3])))
