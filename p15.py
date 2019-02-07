import random

def reservoir_sampling(stream):
    chosen = None 
    for i, elem in enumerate(stream):
        chosen = elem if random.randint(1, i + 1) == 1 else chosen
    return chosen