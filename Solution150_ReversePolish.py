class Solution150_ReversePolish:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            if token in ['+','-','*','/']:

                # 先进行 数字格式 从 str 到 int的转化
                b= int(stack.pop())
                a = int(stack.pop())

                if token=='+':
                    stack.append(a+b)
                elif token=='-':
                    stack.append(a-b)
                elif token=='*':
                    stack.append(a*b)

                elif token=='/':
                    res = 0
                    if (a<0 and b>0)or(a>0 and b<0):

                        res = -(abs(a)//abs(b)) # 解决python 3 中 向下取证问题 先转为 正数 在加一个负号
                    else:
                        res = a//b
                    stack.append(res)
            else:
                stack.append(int(token))

        return int(stack[-1])

"""
总结：
贴下我自己的题解，不同的解决坑的思路，这两个坑运气特别好，自己做的时候都踩到了 第一个坑：关于负数字符串不能判断为数字的问题，
其实可以通过改变if else的顺序去处理，只要字符串在['+','-','*','/']里面就执行相关的计算，如果不是这几个字符 
那肯定就是数字了(踩第一个坑是因为if else 反着放就不行了 因为isdigit()无法判断负数字符串为数字的问题 所以把它放在else语句里面就行了) 
第二个坑：关于python中数字相除下取整的问题，可以在执行除运算时提前判断两个数字是否有且仅有一个负数，如果是 就先进行正数相处（加一个绝对值）
然后再加一个负号就行了python3中的两个坑

"""



if __name__ == '__main__':
    x = Solution150_ReversePolish()

    #s = ["2","1","+","3","*"]
    #s = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    s = ["4","-2","/","2","-3","-","-"]


    result = x.evalRPN(s)
    print(result)





