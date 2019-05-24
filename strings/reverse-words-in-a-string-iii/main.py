class Solution:
    def reverseWords(self, s: str) -> str:
        l, r = 0, 0
        result = ""

        while r < len(s):
            while r < len(s) and s[r] != " ":
                r += 1

            tmp = ""

            while l <= r:
                tmp = s[l] + tmp
                l += 1

            result = result + tmp
            r += 1
            if r < len(s):
                result += " "

        return result
