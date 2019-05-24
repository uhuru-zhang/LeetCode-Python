class Solution:
    digits_to_char = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str):
        if len(digits) == 1:
            return [c for c in self.digits_to_char[digits]]

        result = []

        sub_result = self.letterCombinations(digits[1:])

        for c in self.digits_to_char[digits[0]]:
            for r in sub_result:
                result.append(c + r)
        return sub_result
