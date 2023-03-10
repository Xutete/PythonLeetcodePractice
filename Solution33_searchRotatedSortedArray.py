class Solution:
    def search(self, nums, target):
        # initialize your pointer
        left = 0
        right = len(nums) - 1

        # [1] left and right equal to each other, and we still need to check them
        while left <= right:   # while left + 1 < right or left <= right ？？？？ 问若萱
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            # "left sorted portion"
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # else case are in "right sorted portion"
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


