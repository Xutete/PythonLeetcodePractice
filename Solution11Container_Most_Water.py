

# are limited by the height of shorter line
class Solution11Container_Most_Water:
    def maxArea(self, height):

        r = len(height)
        l = 0
        maxArea_result = 0

        # 互相靠近的挪动
        while l < r:
            width = r - l  # 宽
            maxArea_result = max(maxArea_result, min(height[l], height[r]) * width) # 高 * 宽

            # 移动短的边 因为这个是下限
            if height[l] <= height[r]:
                l += 1

            else:
                r -= 1

        return maxArea_result


