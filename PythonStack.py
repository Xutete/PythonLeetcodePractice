import collections
from collections import deque

stack = []

# append() function to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack[-1])


# pop () function to pop element from stack in LIFO (last-in-first-out)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

if not stack:
    print('yes')


print('\nStack after elements are popped:')
print(stack)


