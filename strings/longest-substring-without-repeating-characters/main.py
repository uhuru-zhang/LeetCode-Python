class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes_dict = {}
        max_length = 0
        left = -1

        for i, c in enumerate(s):
            if c in indexes_dict and indexes_dict[c] >= left:
                left = indexes_dict[c] + 1
            indexes_dict[c] = i
            max_length = max(i - left + 1, max_length)

        return max_length