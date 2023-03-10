class Myqueue:

    def __init__(self):

        '''
        in 主要负责 push, out 主要负责 pop
        '''

        self.stack_in = []
        self.stack_out = []

    def push(self, x):

        '''
        有新元素进来，就往in 里面push
        '''
        self.stack_in.append(x)


    def pop(self):
        '''
        remove the element from in front of queue and returns that element.
        '''

        if self.empty():
            return None

        if self.stack.out:
            return self.stack_out.pop()

        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())

            return self.stack_out.pop()

    # peek: 返回队列首部元素
    def peek(self):
        '''
        Get the front element
        '''
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):

        '''
        只有 in 或者 out 有元素，说明队列不为空
        '''
        return not (self.stack_in or self.stack_out)



