class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [(1000, "M"), (900, "CM"),
                (500, "D"), (400, "CD"),
                (100, "C"), (90, "XC"),
                (50, "L"), (40, "XL"),
                (10, "X"), (9, "IX"),
                (5, "V"), (4, "IV"),
                (1, "I"), ]

        result = ""
        i = 0
        while num != 0:
            if num >= nums[i][0]:
                result += nums[i][1]
                num -= nums[i][0]
            else:
                i += 1
        return result
