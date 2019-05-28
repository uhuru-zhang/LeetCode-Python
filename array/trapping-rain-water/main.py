class Solution:
    def trap(self, height: list) -> int:
        if len(height) <= 1:
            return 0

        max_height = max(height)
        max_index_left = height.index(max_height)
        max_index_right = height.index(max_height, max_index_left + 1) \
            if max_height in height[max_index_left + 1:] \
            else max_index_left

        water, current_water, current_height = 0, 0, 0
        for h in height[:max_index_left + 1]:
            if current_height <= h:
                current_height = h
                water += current_water
                current_water = 0
            else:
                current_water += current_height - h

        current_water, current_height = 0, 0
        for h in reversed(height[max_index_right:]):
            if current_height <= h:
                current_height = h
                water += current_water
                current_water = 0
            else:
                current_water += current_height - h

        for h in height[max_index_left: max_index_right]:
            water += max_height - h
        return water