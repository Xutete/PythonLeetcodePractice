class Solution20_Valid_Parenthese_method2:
    def isValid(self, s):

        stack = []
        # s = '[}'
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')  # stack = [ ']' ]
            elif item == '{':
                stack.append('}')  # stack = [ ']' ]


            # 第二种情况，遍历字符串的过程中，stack已经没有要匹配的字符
            # 第三种情况，遍历字符串的过程中，stack 已经为空
            # not stack 表示已经为空
            elif not stack or stack[-1] != item:
                print(stack)
                return False

            else:
                stack.pop()

        # 第一种情况：已经遍历完了字符串，但是stack 不为空，说明相应的左括号没有右括号来匹配
        return True if not stack else False


if __name__ == '__main__':
    x = Solution20_Valid_Parenthese_method2()

    s = "( [ ] }"
    ValidParentheses_bool = x.isValid(s)
    print(ValidParentheses_bool)
