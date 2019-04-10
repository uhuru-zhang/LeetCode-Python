class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        首先，我们假定从 0 位置开始，运行到 k_0 位置时 油量耗尽 那么 设到 k_0 时候缺少油量为 sum_0
        那么从 k_0 位置 出发 到达 k_1 位置 油量耗尽 此时缺少油量记为 sum_1
        一直到 k_n 个油量耗尽的位置 假设此时油量为 sum_n
        设 经过 k_n 个位置 到达最后最后一站 剩余油量 sum
        那么 如果 sum - sum_0 - sum_1 - ... - sum_n  > 0 那么就可以完成题目中所说循环。
        """
        sum_ = []

        current_sum = 0
        index = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            current_sum += g - c
            if current_sum < 0:
                sum_.append(current_sum)
                current_sum = 0
                index = i + 1

        sum_.append(current_sum)
        if sum(sum_) < 0:
            return -1
        else:
            return index

if __name__ == '__main__':
    s = Solution()
    a = s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
    print(a)
