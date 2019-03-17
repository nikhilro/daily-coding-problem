def segregate(lst): # O(n) time, O(1) space, doesn't guarantee order
    def swap(a, b):
        lst[a], lst[b] = lst[b], lst[a]

    ptrs = { 'R': 0, 'G': 0, 'B': 0 }
    for i, char in enumerate(lst):
        while i != ptrs[char]:
            swap(i, ptrs[char])
            ptrs[char] += 1
            char = lst[i]
        else:
            ptrs[char] += 1

    return lst
        
print(segregate(['G', 'B', 'R', 'R', 'B', 'R', 'G']))

def segregate_ordered(lst): # O(n) time, O(1) space
    def swap(a, b):
        lst[a], lst[b] = lst[b], lst[a]

    i, swaps = 0, { 'B': 0, 'G': 1, 'R': 2 }
    for i, char in enumerate(lst):
        if sum(val for key, val in swaps.items()) < 0:
            break
        if swaps[char] != -1:
            swap(i, swaps[char])
            swaps[char] = -1 
            
    return segregate(lst)

print(segregate_ordered(['G', 'B', 'R', 'R', 'B', 'R', 'G']))

def segregate_ordered2(lst): # O(n) time, O(1) space
    def swap(a, b):
        lst[a], lst[b] = lst[b], lst[a]

    lo, hi = 0, len(lst) - 1
    for i in range(len(lst)):
        if i > hi:
            break
        
        if lst[i] == 'B':
            swap(hi, i)
            hi -= 1 

        if lst[i] == 'R':
            swap(lo, i)
            lo += 1 
        
    return lst 
    
print(segregate_ordered2(['G', 'B', 'R', 'R', 'B', 'R', 'G']))