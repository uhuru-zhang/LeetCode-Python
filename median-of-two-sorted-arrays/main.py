# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        (nums1, nums2) = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        even = (len(nums1) + len(nums2)) % 2 == 0

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        rubbish = int((len(nums1) + len(nums2) + 1) / 2 - 1)
        while rubbish > 0:
            if len(nums1) == 0:
                nums2 = nums2[rubbish:]
                break
            if len(nums2) == 0:
                nums1 = nums1[rubbish:]
                break

            m = max(int(min(int(rubbish / 2), len(nums1))), 1)
            n = max(int(rubbish - m), 1)

            if nums1[m -1] < nums2[n-1]:
                rubbish -= m
                nums1 = nums1[m:]
            else:
                rubbish -= n
                nums2 = nums2[n:]

        nums1 = nums1[:min(len(nums1), 2)]
        nums2 = nums2[:min(len(nums2), 2)]

        nums = sorted(nums1 + nums2)
        if even:
            return sum(nums[:2]) / 2
        return nums[0]

