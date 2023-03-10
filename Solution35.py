class Solution35:
    def searchInsert(self, nums, target) :

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            print(mid)

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid + 1  # lower pointer 增加 1


            else:
                high = mid - 1 # higher pointer 减小 1
               # print(high)

        return low

# Binary search is a search algorithm that find the position of a target value within a sorted array.

if __name__ == '__main__':
    x = Solution35()

    nums = [1,3,5,6]
    target = 2
    output = x.searchInsert(nums,target)
    print(output)








