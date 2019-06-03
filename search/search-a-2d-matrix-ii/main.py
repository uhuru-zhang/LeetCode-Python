class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        index_left, index_right, index_top, index_bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        if index_left == index_right and index_top == index_bottom:
            return matrix[index_top][index_left] == target

        index_row_mid = int((index_top + index_bottom) / 2)
        index_col_mid = int((index_left + index_right) / 2)

        if matrix[index_row_mid][index_col_mid] == target:
            return True
        elif matrix[index_row_mid][index_col_mid] > target:
            return self.searchMatrix(matrix[0:index_row_mid], target) \
                   or self.searchMatrix([m[0:index_col_mid] for m in matrix[index_row_mid:]], target)
        else:
            return self.searchMatrix(matrix[index_row_mid + 1:], target) \
                   or self.searchMatrix([m[index_col_mid + 1:] for m in matrix[0:index_row_mid + 1]], target)