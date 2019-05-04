from collections import defaultdict

def count_attacks(m, bishops): # O(n) time, O(n) space
    ld, rd, count = defaultdict(int), defaultdict(int), 0
    for x, y in bishops:
            count += ld[x - y] + rd[x + y]
            ld[x - y] += 1
            rd[x + y] += 1
    return count

print(count_attacks(5, [(0, 0), (1, 2), (2, 2), (4, 0)]))


