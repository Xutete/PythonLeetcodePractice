class Solution:
    def findMin(self, nums):
        res = nums[0] # initialize result
        left = 0
        right = len(nums) - 1

        while left <= right:
            # nums is not rotated 就是由小到大的顺序
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2  # 注意整除指向的特点
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]: # 注意这边界条件是 包含了 =
                left = mid + 1

            else:
                right = mid - 1

        return res








