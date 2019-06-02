class Solution:
    def findWords(self, board: list, words: list) -> list:
        result = []
        can_not_set = set()
        for w in words:
            can_w = self.exist(board, w)
            result.append(w)
        return result


    def exist(self, board: list, word: str) -> str:
        starts = set()

        self.board = board
        self.visited_set = set()
        self.directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == word[0]:
                    starts.add((i, j))

        if len(word) == 1:
            if len(starts) >= 1:
                return True
        for i, j in starts:
            self.visited_set.add((i, j))
            if self.dfs(i, j, word, 1):
                return True
            self.visited_set.remove((i, j))
        return False

    def dfs(self, i, j, word, w_i):
        for r, c in self.directions:
            next_i, next_j = i + r, j + c

            if next_i < 0 or next_i >= len(self.board) or next_j < 0 or next_j >= len(self.board[0]):
                continue

            if (next_i, next_j) in self.visited_set:
                continue

            if self.board[next_i][next_j] == word[w_i]:
                if len(word) == 1:
                    return word
                else:
                    self.visited_set.add((next_i, next_j))
                    if self.dfs(next_i, next_j, word, w_i + 1):
                        return word
                    self.visited_set.remove((next_i, next_j))

        return word[:w_i + 1]


if __name__ == '__main__':
    s = Solution()
    a = s.exist([["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]], "ABCCED")
    print(a)
