class Solution:
    def __init__(self):
        self.result = []
        self.candidates = []

    def combinationSum2(self, candidates: list, target: int):
        # 采用深度优先搜索，首先将 candidates 进行倒序排列，每次选取 一个值 然后递归搜索 直到找到答案 然后返回选取下一个值继续查找

        candidates = sorted(candidates, reverse=True)
        self.candidates = candidates
        self.dfs(target, [])
        return self.result

    def dfs(self, target: int, result: list):
        if target == 0 and result not in self.result:
            self.result.append(result)

        if len(self.candidates) == 0 or self.candidates[-1] > target:
            return

        for i in range(len(self.candidates)):

            if self.candidates[i] <= target and (len(result) == 0 or self.candidates[i] <= result[-1]):
                c = self.candidates[i]
                self.candidates.pop(i)

                self.dfs(target - c, result + [c])
                self.candidates.insert(i, c)