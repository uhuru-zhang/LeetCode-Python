class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        count = 0

        for num in nums:
            if count == 0:
                result = num

            if result == num:
                count += 1

            else:
                count -= 1

        return result
