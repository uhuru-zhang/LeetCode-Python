class Solution(object):
    def majorityElement(self, nums):
        # 多数投票
        # 任意选择两个数字 假设这两个数字的个数为 cnt1，cnt2 如果 cnt1 + cnt2 > len(nums) * 2/3 则 下述计算过程成立 否则一定不成立
        num1 = num2 = 1e9
        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 += 1
            elif cnt2 == 0:
                num2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        # 找出个数
        cnt1 = nums.count(num1)
        cnt2 = nums.count(num2)
        res = []
        if cnt1 > int(len(nums)/3):
            res.append(num1)
        if cnt2 > int(len(nums)/3):
            res.append(num2)
        return res
