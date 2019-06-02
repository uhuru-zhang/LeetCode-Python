class Solution:
    def isValidSudoku(self, board)-> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        nn_set = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == ".":
                    continue

                if n in row_set[i]:
                    return False
                else:
                    row_set[i].add(n)

                if n in col_set[j]:
                    return False
                else:
                    col_set[j].add(n)

                if n in nn_set[(i // 3) * 3 + (j // 3)]:
                    return False
                else:
                    nn_set[(i // 3) * 3 + (j // 3)].add(n)

        return True
