def max_contiguous_sum(nums):
    m, cur = 0, 0
    for num in nums:
        if num + cur < 0:
            cur = 0
        else:
            cur += num 
        m = max(cur, m)

    return m 

print(max_contiguous_sum([34, -50, 42, 14, -5, 86]), max_contiguous_sum([-5, -1, -8, -9]))

def max_kadane(nums):
    m, cur = 0, 0
    for num in nums:
        cur = max(cur + num, num)
        m = max(cur, m)
    return m 

print(max_kadane([34, -50, 42, 14, -5, 86]), max_kadane([-5, -1, -8, -9]))
