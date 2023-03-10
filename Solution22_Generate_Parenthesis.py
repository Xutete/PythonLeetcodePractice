class Solution22_Generate_Parenthesis:
    def generateParenthesis_1(self, n):

        stack = []
        res = []

        def backtrack(openN, closedN):

            if openN == closedN == n:
                res.append("".join(stack))
                print("temp_res: " + str(res))
                return

            # 先判断 open 数量，如果open < n 则添加一个 open "（"
            if openN < n:
                stack.append("(")
                print("ans1: " + str(stack))

                backtrack(openN + 1, closedN)
                stack.pop()
                print("ans2: " + str(stack))


            if closedN < openN:
                stack.append(")")
                print("ans3: " + str(stack))

                backtrack(openN, closedN + 1)

                stack.pop()
                print("ans4: " + str(stack))

        backtrack(0, 0)
        return res



if __name__ == '__main__':
    n = 1
    print( Solution22_Generate_Parenthesis().generateParenthesis_1(n))

















