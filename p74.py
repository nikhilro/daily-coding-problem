def appearances_naive(n, x): # O(n^2) time, O(1) space
    return sum(1 for i in range(1, n + 1) for j in range(1, n + 1) if i * j == x)

print(appearances_naive(6, 12))

def appearances(n, x): # O(n) time, O(1) space
    return sum(1 for i in range(1, n + 1) if not x % i and x / i <= n)

print(appearances(6, 12))
