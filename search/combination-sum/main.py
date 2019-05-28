class Solution:
    def __init__(self):
        self.result = []
        self.candidates = []

    def combinationSum(self, candidates: list, target: int):
        # 采用深度优先搜索，首先将 candidates 进行倒序排列，每次选取 一个值 然后递归搜索 直到找到答案 然后返回选取下一个值继续查找

        # 排序的目的在于在23行可以去除重复值 如 [5, 1, 2] 和 [5, 2, 1]
        candidates = sorted(candidates, reverse=True)
        self.candidates = candidates
        self.dfs(target, [])
        return self.result

    def dfs(self, target: int, result: list):
        if target == 0:
            self.result.append(result)

        if self.candidates[-1] > target:
            return

        for c in self.candidates:
            if c <= target and (len(result) == 0 or c <= result[-1]):
                self.dfs(target - c, result + [c])