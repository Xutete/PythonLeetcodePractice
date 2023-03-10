class Solution:
    # 不允许用切片
    # 不允许用slicing
    def reverseLeftWords(self, s: str, n: int) -> str:
        def reverse_sub(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        res = list(s)
        end = len(res) - 1
        reverse_sub(res, 0, n - 1) # 反转左边
        reverse_sub(res, n, end) # 反转右边
        reverse_sub(res, 0, end) # 反转所有的
        return ''.join(res)

# 同方法二
# 时间复杂度：O(n)
# 空间复杂度：O(n)，python的string为不可变，需要开辟同样大小的list空间来修改










