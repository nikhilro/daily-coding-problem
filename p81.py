def permutations(mapping, nums): # O(mn) where m is len(nums), n is avg(len(mapping[num])), same for space
    perms = [""]
    for num in nums:
        perms = [old + new for new in mapping[num] for old in perms]
    return perms

print(permutations({'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}, "23"))