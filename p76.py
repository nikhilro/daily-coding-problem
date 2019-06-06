def remove_columns(matrix): # O(n * m) time, O(1) space
    count = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                count += 1
                break
    return count

matrix = ['cba', 'daf', 'ghi']
print(remove_columns(matrix))

matrix = ['abcdef']
print(remove_columns(matrix))

matrix = ['zyx', 'wvu', 'tsr']
print(remove_columns(matrix))