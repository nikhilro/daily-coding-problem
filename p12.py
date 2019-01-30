def unique_ways_to_climb_naive(steps):
    if (steps == 1):
        return 1
    elif (steps == 2):
        return 2
    else:
        return unique_ways_to_climb_naive(steps - 1) + unique_ways_to_climb_naive(steps - 2)


print(unique_ways_to_climb_naive(4))


def unique_ways_to_climb(steps):
    previous, current = 1, 2

    for _ in range(2, steps):
        current, previous = current + previous, current

    return current


print(unique_ways_to_climb(4))


def unique_ways_to_climb_general(steps, climbs):
    cache = [0] * steps

    for c in climbs:
        cache[c - 1] = 1

    for i in range(steps):
        for c in climbs:
            cache[i] += cache[i - c]

    return cache[steps - 1]


print(unique_ways_to_climb_general(4, [1, 2]))

def unique_ways_to_climb_general_golf(steps, climbs):
    cache = [0] * steps

    for c in climbs:
        cache[c - 1] = 1

    for i in range(steps):
        cache[i] += sum([cache[i - c] for c in climbs])

    return cache[steps - 1]


print(unique_ways_to_climb_general_golf(4, [1, 2]))
