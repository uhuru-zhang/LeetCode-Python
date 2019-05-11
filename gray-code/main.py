class Solution:
    def grayCode(self, n: int) -> list:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        sub_result = self.grayCode(n - 1)
        result = [m for m in sub_result]

        for i in range(len(sub_result)):
            m = sub_result[- (i + 1)]
            """
            将 n - 1 产生的序列 倒序 并在前面 +1 插入到原有序列中 
                1. 因为原有序列是格雷编码，所以后半部分+1之后也是各类编码
                2. 因为倒序之后 连接处只差一个1 所以整体也是格雷编码
            """
            result.append(m + 2 ** (n - 1))

        return result