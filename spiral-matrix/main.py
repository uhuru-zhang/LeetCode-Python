class Solution:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def spiralOrder(self, matrix: list) -> list:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        num = len(matrix) * len(matrix[0])

        result = []
        current_direction = 0
        current_indexes = (0, 0)
        flags = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        while num > 0:
            result.append(matrix[current_indexes[0]][current_indexes[1]])
            flags[current_indexes[0]][current_indexes[1]] = True
            num -= 1

            if current_indexes[0] + self.directions[current_direction][0] >= len(matrix) or \
                    current_indexes[1] + self.directions[current_direction][1] >= len(matrix[0]) or \
                flags[current_indexes[0] + self.directions[current_direction][0]][current_indexes[1] + self.directions[current_direction][1]] is True:
                current_direction = (current_direction + 1) % 4

            current_indexes = (current_indexes[0] + self.directions[current_direction][0],
                               current_indexes[1] + self.directions[current_direction][1])

        return result
