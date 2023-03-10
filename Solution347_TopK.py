class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [ [ ] for i in range(len(nums) + 1)] #  +1 是为了 从0 开始 到 nums.size() 为止
        # 比如 nums = [1, 1, 1, 2, 2, 100] nums.size() = 6
        # freq => 这个语句返回了一个 nested list => 初始化为：[ [null] [100] [2] [1] [null] [null] [null]]
        # 里面的list的index 就是 n 出现的次数 里面list 本身 存放的是 n
        # 比如 这个 example 的 freq 就是 []

        for n in nums:
            count[n] = 1 + count.get(n, 0)


        # n是 nums 里面出现到数字，c 是 count计数的数值
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # range(start, stop, step)
        for i in range(len(freq) - 1, 0, -1): # 从后往前找　
            for n in freq[i]: # 这个是确保有的数字 重复出现的次数一样 也能考虑进去
                res.append(n)
                if len(res) == k:
                    return res






