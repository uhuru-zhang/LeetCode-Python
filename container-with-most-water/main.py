class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        return self.maxAreaCore(height, l, r)

    def maxAreaCore(self, height, l, r):
        if r - l <= 0:
            return 0

        area = min(height[l], height[r]) * (r - l)

        while l < r:
            if height[l] < height[r]:
                return max(area, self.maxAreaCore(height, l + 1, r))
            elif height[l] > height[r]:
                return max(area, self.maxAreaCore(height, l, r - 1))
            else:
                return max(area, self.maxAreaCore(height, l + 1, r), self.maxAreaCore(height, l, r - 1))
