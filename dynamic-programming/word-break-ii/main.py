class Solution:
    def __init__(self):
        self.result = []
        self.word_set = set()
        self.max_length = 0

    def wordBreak(self, s: str, wordDict: list) -> list:
        if len(wordDict) == 0 or len(s) == 0:
            return []

        breakp = [0]

        # 只有在有解的时候才去 进行搜索查找
        for i in range(len(s) + 1):
            for j in breakp:
                if s[j:i] in wordDict:
                    breakp.append(i)
                    break
        if breakp[-1] != len(s):
            return []


        self.word_set = set(wordDict)
        self.max_length = len(max(wordDict, key=lambda a: len(a)))

        self.__word_break__(s, [])

        return self.result

    def __word_break__(self, s, current_result):
        if len(s) == 0:
            self.result.append(" ".join(current_result))

        for i in range(1, self.max_length + 1):
            if i > len(s):
                break

            if s[:i] in self.word_set:
                self.__word_break__(s[i:], current_result + [s[:i]])


if __name__ == '__main__':
    s = Solution()
    a = s.wordBreak("catsanddog",
                    ["cat", "cats", "and", "sand", "dog"])
    print(a)
