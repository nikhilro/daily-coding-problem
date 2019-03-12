def trapped_water_very_naive(walls): # O(n*2) time, O(1) space because generator
    return sum(max(min(max(walls[:i]), max(walls[i+1:])) - walls[i], 0) 
                for i in range(1, len(walls) - 1))


print(trapped_water_very_naive([3, 0, 1, 3, 0, 5]))

# wrong but adapted to be correct
# def trapped_water_naive(walls): # O(n) time, O(n) space because generator stack for min_right
#     def min_left(lst, cur_min=walls[0]):
#         for elem in lst:
#             cur_min = min(elem, cur_min)
#             yield cur_min
        
#     def min_right(lst, cur_min=walls[-1]):
#         cur_min = min(lst[-1], cur_min)
#         if len(lst) == 3:
#             yield cur_min
#         else:
#             yield from min_right(lst[:-1], cur_min)
#             yield cur_min
    
#     left, right = min_left(walls), min_right(walls)
#     return sum(max(next(left), next(right)) for _ in range(1, len(walls) - 1))

def trapped_water_naive(walls): # O(n) time, O(1) or O(n) space depending on counting stack usage
    def max_right(lst, cur_max=walls[-1]):
        cur_max = max(lst[-1], cur_max)
        if len(lst) == 3:
            yield cur_max
        else:
            yield from max_right(lst[:-1], cur_max)
            yield cur_max

    def max_left(lst, cur_max=walls[0]):
        for elem in lst:
            cur_max = max(elem, cur_max)
            yield cur_max


    left, right = max_left(walls), max_right(walls)
    return sum(max(min(next(left), next(right)) - walls[i], 0) for i in range(1, len(walls) - 1))

print(trapped_water_naive([3, 0, 1, 3, 0, 5]))

def trapped_water(walls): # O(n) time, O(1) space, not tested
    def max_iter(lst, cur_max):
        for elem in lst:
            cur_max = max(elem, cur_max)
            yield cur_max
    
    # could also use enumerate or walls.index(max(walls))
    max_index = max(range(len(walls)), key=walls.__getitem__)  

    left = max_iter(walls[:max_index], cur_max=walls[1])
    right = max_iter(reversed(walls[max_index + 1:]), cur_max=walls[-1])

    left = sum(max(next(left) - walls[i], 0) for i in range(1, max_index))
    right = sum(max(next(right) - walls[i], 0) for i in range(len(walls) - 2, max_index, -1))

    return left + right