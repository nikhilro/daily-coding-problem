def largest_triplet_product(nums): # O(n) time, O(1) space
    m = sm = tm = mi = smi = 0
    for num in nums:
        if num > m:
            m, sm, tm = num, m, sm 
        elif num > sm:
            sm, tm = num, sm 
        elif num > tm:
            tm = num 
        if num < mi:
            mi, smi = num, mi
        elif num < smi:
            smi = num 
    return max(m * sm * tm, mi * smi * m)

print(largest_triplet_product([-10, -10, 5, 2]))