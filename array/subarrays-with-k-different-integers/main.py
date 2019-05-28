from collections import Counter


# 虽然超时 但是个人感觉还是这个比较好
class Solution:
    def subarraysWithKDistinct(self, A: list, K: int) -> int:
        if len(A) < K or len(A) == 0 or K == 0:
            return 0

        result = 0

        for i in range(len(A) - K + 1):
            result_set = set(A[i: i + K])
            for j in range(i + K - 1, len(A)):
                result_set.add(A[j])
                if len(result_set) == K:
                    result += 1
                if len(result_set) > K:
                    break

        return result


#
#
# class Solution:
#     def subarraysWithKDistinct(self, A: list, K: int) -> int:
#         if len(A) < K or len(A) == 0 or K == 0:
#             return 0
#
#         result = 0
#         result_dict = Counter()
#         start_index = 0
#         i = 0
#         while i < len(A) and start_index < len(A):
#             result_dict[A[i]] += 1
#             if len(result_dict) == K:
#                 current_left = start_index
#                 while len(result_dict) == K and current_left <= i:
#                     result_dict[A[current_left]] -= 1
#                     if result_dict[A[current_left]] == 0:
#                         del result_dict[A[current_left]]
#                     current_left += 1
#
#                     result += 1
#                 current_left -= 1
#                 while current_left >= start_index:
#                     result_dict[A[current_left]] += 1
#                     current_left -= 1
#
#             if len(result_dict) == K + 1:
#                 while len(result_dict) == K + 1 and start_index < len(A):
#                     result_dict[A[start_index]] -= 1
#                     if result_dict[A[start_index]] == 0:
#                         del result_dict[A[start_index]]
#                     start_index += 1
#                 result_dict[A[i]] -= 1
#                 if result_dict[A[i]] == 0:
#                     del result_dict[A[i]]
#                 i -= 1
#
#             i += 1
#
#         return result


if __name__ == '__main__':
    s = Solution()
    # b = s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2)
    b = s.subarraysWithKDistinct([2, 1, 1, 1, 2], 1)
    print(b)
