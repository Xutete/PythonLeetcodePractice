class Solution:
    def minSubArrayLen(self, target, nums):

        # Initialize length with infinity
        maxValue = float('inf')
        length = maxValue

        i = 0 # 右边界
        j = 0 # 左边界

        sum = 0

        while(j < len(nums)):
            sum += nums[j]

            # If sum so far is >= target, find what is the smallest length of subarray we can get from this window
            # which fulfills the condition
            if (sum >= target):
                while (sum >= target):
                    length = min(length, j - i + 1) # 注意python index 的问题

                    # Shrink the window from left side, if sum > target value (如果还在window里面, 则)
                    sum -= nums[i]
                    i += 1

            # Increase the window size from right size
            j += 1

            # If length is still infinity, that means we did not get any subarray that fullfills this condition so in
            # that case we can return 0

        return 0 if length == maxValue else length

