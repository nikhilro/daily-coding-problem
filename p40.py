import string, math
digits = string.digits + string.ascii_lowercase

def find_unique_naive(nums): # O(n) time, O(n) space
    count = {} 
    for num in nums:
        if num in count:
            count[num] += 1
        else: 
            count[num] = 1
        if count[num] == 3:
            count.pop(num)
    return [*count][0]

print(find_unique_naive([6, 1, 3, 3, 3, 6, 6]))
print(find_unique_naive([13, 19, 13, 13]))  

def find_unique_naive2(nums): # O(n^2) time, O(1) space
    for num in nums:
        count = len(list(filter(lambda x: x == num, nums)))
        if count == 1:
            return num

print(find_unique_naive2([6, 1, 3, 3, 3, 6, 6]))
print(find_unique_naive2([13, 19, 13, 13]))  

def find_unique(nums): # O(n) time, O(1) space
    def posint2base(x, base):
        if x == 0:
            return 0
        
        rem, d = x, []
        while rem:
            d.append(rem % base)
            rem = rem // base
            
        return list(reversed(d))
    
    def lst3mod(nums):
        return [num % 3 for num in nums] 

    def add2lsts(lst1, lst2):
        if len(lst1) < len(lst2):
            lst1, lst2 = lst2, lst1
        if not lst2:
            return lst1
            
        lst1[-len(lst2):] = [num + lst1[-len(lst2)+i] for i, num in enumerate(lst2)]
        return lst1

    x3 = []
    for num in nums:
        x3 = lst3mod(add2lsts(posint2base(num, 3), x3))
    
    return int("".join([str(num) for num in x3]), base=3)

print(find_unique([6, 1, 3, 3, 3, 6, 6]))
print(find_unique([13, 19, 13, 13]))  
        
def find_unique_cleaner(nums): # O(n) time, O(1) space
    result = [0] * 32
    for num in nums:
        for i in range(int(math.log(num, 2)) + 1):
            bit = num >> i & 1 
            result[i] = (result[i] + bit) % 3 
    return int("".join(str(num) for num in reversed(result)), 2)
    
print(find_unique_cleaner([6, 1, 3, 3, 3, 6, 6]))
print(find_unique_cleaner([13, 19, 13, 13]))  
        
    