# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    """
    代码思路如下：
        我们将找中位数变换为从数组中去除比中位数小的所有数字。
        我们设两个数组分别长度为 a,b 去掉的数字个数为 m,n 并令 m + n = rubbish。rubbish = (a + b + 1) / 2 -1
        我们每次循环都尝试比较 nums[m - 1] 和 nums[n - 1] 选择其中的较小者，将较小者所在数组的前m(或n)个数字去掉，直到去掉了rubbish个数字,或者某一个数组被清空。
        我们每一次删除数据的时候都可以保证有 (a + b) - (m + n) + 1 个数据大于被减去的数据中的最大值，也就是保证被减去的数据，一定小于中位数。
        我们每次令 m 和 n 大致等于 rubbish / 2，这样就可以保证 log(m+n)的时间复杂度。

    """
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

