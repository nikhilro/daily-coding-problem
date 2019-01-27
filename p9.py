def largest_non_adjacent_sum(nums):
    prev_max = nums[0]
    current_max = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current_max, prev_max = max(current_max, prev_max + nums[i]), current_max
    
    return current_max

nums = [2, 4, 6, 2, 5]
print(largest_non_adjacent_sum(nums))
nums = [5, 1, 1, 5]
print(largest_non_adjacent_sum(nums))