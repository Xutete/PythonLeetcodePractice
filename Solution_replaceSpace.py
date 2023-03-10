class Solution:
    def replaceSpace(self, s: str):
        '''
        输入：s = "We are happy."
        输出："We%20are%20happy."
        '''

        list_s = list(s)
        stack = []

        for idx in range(len(list_s)):
            if list_s[idx] == " ":
                stack.append("%")
                stack.append("2")
                stack.append("0")
            else:
                stack.append(list_s[idx])

            idx += 1

        return "".join(stack)


if __name__ == '__main__':
    x = Solution()

    s = "We are happy."

    result = x.replaceSpace(s)

    print(result)





