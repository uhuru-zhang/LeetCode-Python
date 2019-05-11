from functools import reduce


class Solution:
    def singleNumber(self, nums: list) -> int:
        return reduce(lambda a, b: a & b, nums)