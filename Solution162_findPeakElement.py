class Solution:
    def findPeakElement(self, nums):
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        left, right, ans = 0, n - 1, -1

        while left <= right:
            mid = (left + right) // 2

            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid

                break  # 找到了答案就可以break

            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return ans



ob1 = Solution()
print(ob1.findPeakElement([15,35,85,96,5,6,8,12]))