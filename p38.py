def queen_arrangements(n): # O(n^n) time, O(1) space
    rows, diag_s, diag_d = set(), set(), set()
    count = 0

    def helper(col):
        if col >= n:
            nonlocal count 
            count += 1
            return

        for i in range(n):
            if i not in rows and i + col not in diag_s and i - col not in diag_d:
                rows.add(i)
                diag_s.add(i + col)
                diag_d.add(i - col)
                helper(col+1)
                rows.remove(i)
                diag_s.remove(i + col)
                diag_d.remove(i - col)
        
    helper(0)
    return count 

print(queen_arrangements(4))

def queen_arrangements_bitwise(n): # not tested
    count, done = 0, 2**n - 1 

    def helper(rows, diag, anti_diag):
        nonlocal count

        if rows == done:
            count += 1 
            return
        
        open_pos = ~(rows | diag | anti_diag)

        while open_pos:
            q_pos = open_pos & -open_pos
            open_pos -= q_pos
            helper(rows | q_pos, (diag | q_pos)<<1, (anti_diag | q_pos)>>1)

    return count