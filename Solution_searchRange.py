class Solution:
    def search_range(self, a, target):
        # write your code here
        if not a: # 如果是一个empty
            return [-1, -1]
        left = 0
        right = len(a) - 1
        start = -1
        while left < right: # 边界条件1 —> 两个不能相等
            mid = (left + right) // 2

            if a[mid] >= target: # 边界条件2 -> mid值 >= target 搜索mid左边 "值小的部分"
                right = mid
            else: # mid值 < target 搜索mid右边 "值大的部分"
                left = mid + 1

        if a[left] != target:
            return [-1, -1]

        start = left
        
        while left < len(a) and a[left] == target:
            left += 1
        return [start, left - 1]



if __name__ == '__main__':
    x = Solution()

    #a = []
    a = [5, 7, 7, 8, 8, 10]
    target = 8
    result = x.search_range(a, 8)
    print(result)



