class Solution:
    # 1.移除多余的空格 -> 我的发现 用了很多 while 而不是 for 循环
    def trim_spaces(self, s):
        n = len(s)
        left = 0
        right = n - 1

        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right = right - 1

        tmp = [] # tmp 是一个stack [] -> 这里使用了 "栈" 的特性
        while left <= right:
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ': # 如果stack[] 最前面的元素不是空格 则添加 当前 元素
                tmp.append(s[left])

            left += 1

        return tmp

    # 2.翻转字符数组 ->
    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None

    # 3.翻转每个单词 ->
    def reverse_each_word(self, nums):

        # 全局变量
        start = 0
        end = 0
        n = len(nums)

        # 注意这种 < or <= 的边界条件
        # 是不是也可以用 start <= n - 1
        while start < n:
            # 这么找到一个单词的结尾呢？ -> 靠 ' ' 空格
            while end < n and nums[end] != ' ':
                end += 1

            # 当找到了 一个单词的结尾后
            # 使用反转 -> reverse_string()
            self.reverse_string(nums, start, end - 1)
            # 反转结束 跳过下一个 空格 ' ' 找到下一个单词的 起点
            start = end + 1
            end += 1

        return None



    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverse_string(l, 0, len(l) - 1)
        self.reverse_each_word(l)
        return ''.join(l) # '' 别写成 ' '



















