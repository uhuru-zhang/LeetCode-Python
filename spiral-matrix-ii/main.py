class Solution:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def generateMatrix(self, n: int) -> list:
        num = 1

        result = [[0 for _ in range(n)] for _ in range(n)]
        current_direction = 0
        current_indexes = (0, 0)
        while num <= n ** 2:
            result[current_indexes[0]][current_indexes[1]] = num
            num += 1

            if current_indexes[0] + self.directions[current_direction][0] >= len(result) or \
                    current_indexes[1] + self.directions[current_direction][1] >= len(result[0]) or \
                    result[current_indexes[0] + self.directions[current_direction][0]][
                        current_indexes[1] + self.directions[current_direction][1]] != 0:
                current_direction = (current_direction + 1) % 4

            current_indexes = (current_indexes[0] + self.directions[current_direction][0],
                               current_indexes[1] + self.directions[current_direction][1])

        return result
