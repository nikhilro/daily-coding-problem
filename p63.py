def find_word(matrix, target):  # O(m * n) time, O(1) space
    def check_lr(i, j):
        rl = len(matrix[i])
        for c, char in enumerate(target):
            if c + j >= rl or matrix[i][c + j] != char:
                return False
        return True
    
    def check_tb(i, j):
        cl = len(matrix)
        for c, char in enumerate(target):
            if c + i >= cl or matrix[c + i][j] != char:
                return False
        return True
    
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == target[0]:
                # if "".join(row[j:]) == target or "".join(r[j] for r in matrix[i:]) == target:
                if check_lr(i, j) or check_tb(i, j):
                    return True
    return False


matrix =[['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]
print(find_word(matrix, 'FOAM'), find_word(matrix, 'MASS'))

# kinda neat if checking length before
#     for c1, c2 in zip(word, (matrix[i][c] for i in range(r, col_len))):
#         if c1 != c2:
#             return False