def increasing_length_first(arr): # O(n^2) time, O(n) space
    cache, longest = [1] * len(arr), 0

    for i in reversed(range(len(arr) - 1)):
        following = max(cache[j] for j in range(i, len(arr)) if arr[j] > arr[i])
        cache[i] += following
        longest = max(cache[i], longest)
    
    return longest

print(increasing_length_first([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

def increasing_length_not_golf(arr):
    cache, longest = [1] * len(arr), 0
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
        longest = max(cache[i], longest)
    return longest

def increasing_length_golf(arr):
    cache, longest = [1] * len(arr), 0
    for i in range(1, len(arr)):
        cache[i] += max(cache[j] for j in range(i) if arr[i] > arr[j])
        longest = max(cache[i], longest)
    return longest

def increasing_length_stupidly_golf(arr):
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        cache[i] += max(cache[j] for j in range(i) if arr[i] > arr[j])
    return max(cache)