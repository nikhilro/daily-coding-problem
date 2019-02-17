def min_(arr):
    '''returns two mins and their indices'''
    min, second_min = ((0, arr[0]), (1, arr[1])) \
        if arr[0] < arr[1] else ((1, arr[1]), (0, arr[0]))

    for i, elem in enumerate(arr[2:], 2):
        if elem <= min[1]:
            second_min = min[:]
            min = (i, elem)
        elif elem <= second_min[1]:
            second_min = (i, elem)
    
    return min, second_min

# sanity check
print(min_([1, 2, 3, 4, 1]))

# not tested
def min_cost_houses(cost_matrix): # run: O(n * k), space: O(1)
    first_strand, second_strand = min_(cost_matrix[0])

    for costs in cost_matrix[1:]:
        next_min, next_second_min = min_(costs)

        # minimize each strand
        if first_strand[0] != next_min[0]:
            first_strand = (first_strand[1] + next_min[1], next_min[0])
        else: # first_strand must != next_second_min index if == next_min index
            first_strand = (first_strand[1] + next_second_min[1], next_second_min[0])
        
        if second_strand[0] != next_min[0]:
            second_strand = (second_strand[1] + next_min[1], next_min[0])
        else: # second_strand must != next_second_min index if == next_min index
            second_strand = (second_strand[1] + next_second_min[1], next_second_min[0]) 
        
    return first_strand[1] if first_strand[1] < second_strand[1] else second_strand[1]