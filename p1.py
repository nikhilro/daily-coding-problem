def two_sum(lst, k): # O(N) runtime, O(N) space
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False

lst = [10, 15, 3, 7]
k = 17

print(two_sum(lst, k))