# Naive sol: brute force for every possible substring: O(n^2 * k) 

def longest_distinct_substring(s, max_chars): 
    if max_chars <= 0:
        return 0

    current_chars = {}
    indices = [0] # can be improved, don't need all indices 

    for index, char in enumerate(s):
        if len(current_chars) < max_chars or char in current_chars:
            current_chars[char] = index
        else:
            indices.append(index - 1)
            farthest = min(current_chars, key = current_chars.get)
            indices.append(current_chars[farthest] + 1)
            del current_chars[farthest]
            current_chars[char] = index

    indices.append(len(s) - 1)

    max_index = 0
    for i in range(0, len(indices), 2):
        if indices[i+1] - indices[i] > indices[max_index + 1] - indices[max_index]:
            max_index = i
    
    return s[indices[max_index]: indices[max_index + 1] + 1]

print(longest_distinct_substring("abcba", 2))

def longest_distinct_substring_length(s, max_chars): 
    if max_chars <= 0:
        return 0

    current_chars = {}
    bounds = (0, 0)
    max_length = 0 

    for index, char in enumerate(s):
        current_chars[char] = index
        if len(current_chars) <= max_chars:
            lower_bound = bounds[0]
        else:
            farthest = min(current_chars, key = current_chars.get)
            lower_bound = current_chars[farthest] + 1
            del current_chars[farthest]
        
        bounds = (lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length

print(longest_distinct_substring_length("abcba", 2))
