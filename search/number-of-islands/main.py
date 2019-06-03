class Solution:
    def numIslands(self, grid: list) -> int:
        if len(grid) == 0:
            return 0

        result = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue

                current_sets = set()
                for d in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    if i + d[0] < 0 or i + d[1] >= len(grid) or j + d[1] < 0 or j + d[1] >= len(grid[0]):
                        continue
                    for i_1, s in enumerate(result):
                        if (i + d[0], j + d[1]) in s:
                            current_sets.add(i_1)

                if len(current_sets) == 0:
                    result.append({(i, j)})
                else:
                    set_index = current_sets.pop()
                    result[set_index].add((i, j))
                    for i_2 in current_sets:
                        result[set_index].update(result[i_2])
                        result.pop(i_2)

        return len(result)


if __name__ == '__main__':
    s = Solution()
    a = s.numIslands([["1","0","1","1","0","1","1"]]

                     )
    print(a)
