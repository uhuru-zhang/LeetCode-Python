class Solution:
    def numMatchingSubseq(self, S: str, words) -> int:
        res = 0
        d = {}
        for i in range(len(words)):
            if words[i][0] in d:
                d[words[i][0]].append([i, 0])
            else:
                d[words[i][0]] = [[i, 0]]
        for s in S:
            if s not in d:
                continue
            cur = d[s]
            d[s] = []
            for [i, j] in cur:
                if j == len(words[i]) - 1:
                    res += 1
                else:
                    if words[i][j + 1] in d:
                        d[words[i][j + 1]].append([i, j + 1])
                    else:
                        d[words[i][j + 1]] = [[i, j + 1]]
        return res
