class Solution1047_removeDuplicates:
    def removeDuplicates(self, s):
        stack = []

        for item in s:
            #stack.append(item)

            # if stack 表示 if stack 非空
            if stack and stack[-1] == item:
                stack.pop()

            else:
                stack.append(item)

        # 写错了下面
        return "".join(stack) # 字符串拼接

'''
总结1：注意pop() 应该放在哪个if 条件下
总结2：注意后面需要返回字符串 所以要用 join 做字符串拼接 
'''


if __name__ == '__main__':
    x = Solution1047_removeDuplicates()

    s = "a"
    result = x.removeDuplicates(s)
    print(result)