def solve(sudoku): # O(n^3) time, O(n^2) space
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    blocks = [set() for _ in range(9)]

    def block(i, j):
        return 3 * (i // 3) + j // 3 

    def traverse(i, j):
        if i >= len(sudoku):
            return sudoku
        if j >= len(sudoku[0]):
            return traverse(i + 1, 0)
        if not sudoku[i][j]:
            num = sudoku[i][j]
            if num not in rows[i] and num not in columns[j] and num not in blocks[block(i, j)]:
                rows[i].add(num)
                columns[j].add(num)
                blocks[block(i, j)].add(num)
                return traverse(i, j + 1)
        else:
            for num in range(9):
                if num not in rows[i] and num not in columns[j] and num not in blocks[block(i, j)]:
                    rows[i].add(num)
                    columns[j].add(num)
                    blocks[block(i, j)].add(num)
                    sudoku[i][j] = num
                    attempt = traverse(i, j + 1)
                    if attempt is not None:
                        return attempt
                    else:
                        rows[i].remove(num)
                        columns[j].remove(num)
                        blocks[block(i, j)].remove(num)

    return traverse(0, 0)


