def set_sum_naive(nums, target): # O(2^n * n) time, O(n) space
    def helper(left, s, i):
        if not left:
            return s
        if i == len(nums) or left < 0:
            return 
        attempt = helper(left - nums[i], s + [i], i + 1) # inline append O(n)
        return attempt or helper(left, s, i + 1) 

    s = helper(target, [], 0)
    if s is not None:
        return [nums[i] for i in s]

print(set_sum_naive([12, 1, 61, 5, 9, 2], 24))

def set_sum_naive2(nums, target): # O(2^n) time, O(n) space
    s = [0] * len(nums)
    def helper(left, i):
        if not left:
            return 1
        if i == len(nums) or left < 0:
            return 
        
        s[i] = 1
        attempt = helper(left - nums[i], i + 1)
        if attempt is not None:
            return attempt
        
        s[i] = 0
        return helper(left, i + 1)

    helper(target, 0)
    if s is not None:
        return [nums[i] for i in range(len(s)) if s[i] != 0]

print(set_sum_naive2([12, 1, 61, 5, 9, 2], 24))

def set_sum_naive3(nums, target): # O(2^n) time, O(1) space
    s = 0 
    def helper(left, i):
        if not left:
            return 1
        if i == len(nums) or left < 0:
            return 
        
        nonlocal s 
        s = s | 1 << i 
        attempt = helper(left - nums[i], i + 1)
        if attempt is not None:
            return attempt
        
        s = s & ~(1 << i)
        return helper(left, i + 1)

    helper(target, 0)
    if s:
        return [nums[i] for i in range(len(nums)) if (s & 1 << i) != 0]
    
print(set_sum_naive3([12, 1, 61, 5, 9, 2], 24))

def set_sum(nums, target): # O(n*k) time, O(n*k) space, not sure fully correct since we lose knowledge of some old options as we iterate
    mem = [[0] * (len(nums) + 1) for _ in range(target + 1)]
    for i, num in enumerate(nums, 1):
        for j in range(target + 1):
            if j >= num and mem[j - num][i - 1]: # losing option if mem[j][i - 1] was valid without num
                mem[j][i] = mem[j - num][i - 1] | (1 << (i - 1))
            elif mem[j][i - 1]:
                mem[j][i] = mem[j][i - 1]
            elif j == num:
                mem[j][i] = 1 << (i - 1) 
    if mem[-1][-1]:
        return [nums[i] for i in range(len(nums)) if (mem[-1][-1] & 1 << i) != 0]

print(set_sum([12, 1, 61, 5, 9, 2], 24))
        
        
        
