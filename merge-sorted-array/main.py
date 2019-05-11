class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        i = m - 1
        j = n - 1

        index = m + n - 1
        while j >= 0:
            if i < 0 or nums1[i] <= nums2[j]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index -= 1