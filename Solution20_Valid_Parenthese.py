
class Solution20_Valid_Parenthese:
    def isValid(self, s: str) -> bool:

        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False


        openers = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:

            # 如果 char 在字典中 就 append ： 字典找的是key
            if char in openers:
                stack.append(char)

            else:

                if stack == [] or openers[stack.pop()] != char:
                    return False

        return len(stack) == 0 # return true if active length = 0



if __name__ == '__main__':
    x = Solution20_Valid_Parenthese()

    s = "()"
    ValidParentheses_bool = x.isValid(s)
    print(ValidParentheses_bool)
