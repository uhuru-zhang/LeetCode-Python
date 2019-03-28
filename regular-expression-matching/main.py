
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        index_left, index_right = 0, len(matrix) * len(matrix[0]) - 1

        while index_left <= index_right:
            mid = int((index_left + index_right) / 2)
            i, j = self.oneline_2_mn(mid, len(matrix[0]))
            if index_left == index_right:
                return matrix[i][j] == target

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                index_right = mid - 1
            else:
                index_left = mid + 1
        return False

    def oneline_2_mn(self, oneline_index, n):
        row = (oneline_index + 1) // n + (1 if (oneline_index + 1) % n else 0)
        col = (oneline_index + 1) % n

        return int(row - 1), int(col - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13))
