from operator import itemgetter


class Solution:
    def merge(self, intervals: list) -> list:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=itemgetter(0, 1))

        result = [intervals[0]]
        intervals.pop(0)

        while len(intervals) > 0:
            if intervals[0][0] > result[-1][1]:
                result.append(intervals[0])
            else:
                result[-1] = [result[-1][0], max(result[-1][1], intervals[0][1])]

            intervals.pop(0)

        return result
