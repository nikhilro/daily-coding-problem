def power_set(s): # O(2*n) time and time to generate all permutations
    if not s:
        return [()]
    elem = s.pop()
    sets = power_set(s) 
    return sets + [subset + (elem,) for subset in sets]


print(power_set(set([1, 2, 3])))

def power_set_golf(s):
    if not s:
        return [[]]
    sets = power_set_golf(s[1:])
    return sets + [subset + [s[0]] for subset in sets]

print(power_set_golf([1, 2, 3]))
