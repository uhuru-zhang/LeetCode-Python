class Solution:
    def __init__(self):
        self.reslist = []

    def generateParenthesis(self, n: int):
        self.reslist = []
        sarr = []
        self.__backtrack(n, 0, 0, sarr)
        return self.reslist

    def __backtrack(self, n, pairnum, leftnum, sarr):
        '''
        回溯
        :param pairnum: 已匹配的括号数
        :param leftnum: 未匹配的左括号数目
        :param sarr: 当前字符串
        '''
        if pairnum == n:  # 叶子节点
            # print(sarr)
            self.reslist.append("".join(sarr))
            return
        # left-subtree
        if pairnum + leftnum < n:  # 左括号总数目 < n
            sarr.append("(")
            self.__backtrack(n, pairnum, leftnum + 1, sarr)
            sarr.pop()
        # right-)
        if leftnum > 0:
            sarr.append(")")
            self.__backtrack(n, pairnum + 1, leftnum - 1, sarr)
            sarr.pop()