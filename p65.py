# def print_clockwise(matrix):
#     mode, n, m = 'right', len(matrix), len(matrix[0])
#     for i in range(2, min(m, n) + 1, 2):
#         counter, index, total_vals = 0, 0, 2 * (m - i - 2) + 2 * (n - i)
#         while counter < total_vals:
#             if mode == 'right':
#                 print(matrix[i // 2 - 1][i - 2 + index])
#                 index += 1 
#                 if index > (m - i - 2)
# too many contraints to worry about

def print_clockwise(matrix):
    i, j, offset, n, m, mode, skip = 0, -1, 0, len(matrix) - 1, len(matrix[0]) - 1, 'left', False
    while offset < (min(m, n) + 1) // 2:
        if mode == 'left': 
            if j >= m - offset:
                mode = 'down'
            else:
                j += 1
        if mode == 'down':
            if i >= n - offset:
                mode = 'right' 
            else:
                i += 1
        if mode == 'right':
            if j <= offset:
                mode = 'up'
            else:
                j -= 1
        if mode == 'up':
            if i <= offset + 1:
                mode, skip, offset = 'left', True, offset + 1
            else:
                i -= 1
        if not skip:
            print(matrix[i][j])
        else:
            skip = False
        
    if (min(m, n) + 1) % 2:
        if m == min(m, n):
            j += 1
            for i in range(i, n - offset + 1):
                print(matrix[i][j])
        else:
            for j in range(j + 1, m - offset + 1):
                print(matrix[i][j])

matrix = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

print_clockwise(matrix)