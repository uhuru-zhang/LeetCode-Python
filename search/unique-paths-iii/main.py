class Solution:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self):
        self.result = []

    def uniquePathsIII(self, grid: list) -> int:
        self.grid = grid

        n = 0  # n 代表着路径长度
        i, j = 0, 0  # i,j 代表着起始位置
        for r, row in enumerate(grid):
            for c, num in enumerate(row):
                if num == 0:
                    n += 1
                elif num == 1:
                    i, j = r, c

        #  深度优先搜索
        self.__unique_path__(n + 1, i, j, [])
        return len(self.result)

    def __unique_path__(self, n, i, j, path):
        for d in self.directions:
            #  遍历四个方向
            next_i, next_j = i + d[0], j + d[1]

            #  数组越界
            if next_i < 0 or next_i >= len(self.grid) or next_j < 0 or next_j >= len(self.grid[0]):
                continue

            #  如果到达了终点
            if n == 1 and self.grid[next_i][next_j] == 2:
                    self.result.append(path + [next_i, next_j])
                    continue
            #  如果没有到达终点，则继续寻找
            if self.grid[next_i][next_j] == 0:
                self.grid[i][j] = -1
                self.__unique_path__(n - 1, next_i, next_j, path + [i, j])
                self.grid[i][j] = 0


if __name__ == '__main__':
    s = Solution()
    a = s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]])
    print(a)
