class Solution15_3Sum:
    def threeSum(self, nums):

        # sort the given array
        nums.sort()

        result = []

        # 给其他两个pointer 留空间
        for num1Idx in range(len(nums) - 2):

            # Skip all duplicates from left
            # num1Idx > ensures this check is made only from 2nd elements onwards

            if num1Idx > 0 and nums[num1Idx] == nums[num1Idx - 1]:
                continue # break 是直接跳出循环，continue是当前loop结束 进入下一个loop 也就是 numIdx 继续往前走


            (num2Idx, num3Idx) = (num1Idx + 1, len(nums) - 1)


            while num2Idx < num3Idx:
                sum = nums[num1Idx] + nums[num2Idx] + nums[num3Idx]

                if sum == 0:

                    # Add triplet to result
                    result.append((nums[num1Idx], nums[num2Idx], nums[num3Idx]))

                    num3Idx -= 1

                    # skip all duplicates from right
                    # 当 num2Idx < num3Idx 并且 当前num3Idx 与 过去num3Index + 1  想等，继续移动 num3Index
                    while num2Idx < num3Idx and nums[num3Idx] == nums[num3Idx + 1]:
                        num3Idx -= 1

                elif sum > 0:
                    # Decrement num3Idx to reduce the sum value
                    num3Idx -= 1
                else:
                    # Increment num2Idx to increase the sum value
                    num2Idx += 1

            return result


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(Solution15_3Sum().threeSum(nums))




