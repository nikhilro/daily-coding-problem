def can_subset(nums, target): # O(n * k) time, O(k) space where n is len(nums) and k is target
    sums = [0 for _ in range(target + 1)]
    for num in nums:
        for i, partial in enumerate(sums):
            if partial and i + num <= target:
                sums[i + num] = 1
            elif not partial:
                sums[num] = 1 
            if sums[target]:
                return True
    return False

def can_split_equally(nums):
    s = sum(nums)
    return can_subset(nums, s // 2) if s % 2 == 0 else False
    
print(can_split_equally([15, 5, 20, 10, 35, 15, 10]), can_split_equally([15, 5, 20, 10, 35]))
