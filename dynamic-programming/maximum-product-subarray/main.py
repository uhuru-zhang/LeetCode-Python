class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A), max(B))


if __name__ == '__main__':
    s = Solution()
    a = s.maxProduct([2, 3, -2, 4])
    print(a)
