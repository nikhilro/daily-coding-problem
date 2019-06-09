def count_islands(matrix):  # O(mn) time, O(mn) space
    count, visited = 0, set() 

    def is_water(i, j):
        return not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])
                    and matrix[i][j] == 1)

    def is_new_island(i, j):
        nonlocal count

        visited.add((i, j))

        for di, dj in [(-1, -1), (-1, 0), (-1, 1),
                        (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
            if not is_water(i + di, j + dj) and (i + di, j + dj) in visited:
                    return

        count += 1
        
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                is_new_island(i, j)

    # sum(1 for i in range(len(matrix)) for j in range(len(matrix[0])) if is_island(i, j))
    return count


matrix = [[1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1]]

print(count_islands(matrix))
