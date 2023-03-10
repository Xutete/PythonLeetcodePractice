class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 2, x // 2 # 两个指针的范围

        while left <= right:
            pivot = (left + left)//2
            num = pivot * pivot
            if x < num:
                right = pivot - 1 # 找左半边

            elif x > num:
                left = pivot + 1

            else:
                return pivot


        return

