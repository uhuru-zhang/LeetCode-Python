from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        result_dict = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            result_dict[sorted_s].append(s)

        return list(result_dict.values())