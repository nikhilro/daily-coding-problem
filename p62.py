from scipy.special import comb

def choose(m, n):
    acc_m, acc_n = 1, 1
    for i in range(n):
        acc_m, acc_n = acc_m * (m - i), acc_n * (n - i)
    return acc_m // acc_n

def paths(m, n): # O(n) time, O(1) space
    return comb(m + n - 2, min(m - 1, n - 1)) # choose(m + n - 2, m - 1)

def paths_cs(m, n): # bad time, O(1) space barring callstack
    if m <= 1 and n <= 1:
        return 1 
    elif m > 1 and n > 1:
        return paths_cs(m - 1, n) + paths_cs(m, n - 1)
    elif m > 1:
        return paths_cs(m - 1, n)
    elif n > 1:
        return paths_cs(m, n - 1)

def paths_cs_mem(m, n):  # O(m * n) time, O(m * n) space barring callstack
    cache = [[0] * (max(m, n) + 1) for _ in range(max(m, n) + 1)]
    def helper(m, n):
        if cache[m][n] or cache[n][m]:
            return cache[m][n] or cache[n][m]
        if m <= 1 and n <= 1:
            return 1 
        elif m > 1 and n > 1:
            cache[m][n] = paths_cs(m - 1, n) + paths_cs(m, n - 1)
            return cache[m][n] or cache[n][m]
        elif m > 1:
            cache[m][n] = paths_cs(m - 1, n)
            return cache[m][n] 
        elif n > 1:
            cache[m][n] = paths_cs(m, n - 1)
            return cache[m][n]
        
    return helper(m, n)

print(paths(5, 5), paths_cs(5, 5), paths_cs_mem(5, 5))