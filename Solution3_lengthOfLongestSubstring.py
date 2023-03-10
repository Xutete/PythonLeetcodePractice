from collections import Counter

class Solution3_lengthOfLongestSubstring:
    def lengthOfLongestSubstring(self, s):

        longstr = ''
        r = 0
        l = 0
        maxlen = 0


        while r < len(s):
            if s[r] not in longstr: # 如何判断 string 中是否存在 某个元素
                longstr += s[r]  # 添加这个元素
                r += 1 # 右指针 滑动


            else:
                l += 1 # 如果存在这个元素 则 左指针 滑动
                r = l  # 左右指针回到同一个起点


                if len(longstr) > maxlen: # 判断 目前已经存取的 longstr 是否大于 maxlen
                    maxlen = len(longstr) # 如果大于 则更新

                longstr = '' # 找到当前的最长不重复string 后 初始化longstr

        print (longstr)

        return (max(maxlen, len(longstr))) # maxlen 存下当前已经取到到最长不重复string




if __name__ == '__main__':

    x = Solution3_lengthOfLongestSubstring()
    s = "pwwkew"
    result = x.lengthOfLongestSubstring(s)
    print(result)



