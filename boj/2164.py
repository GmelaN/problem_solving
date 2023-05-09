from sys import stdin
from collections import deque

N = int(stdin.readline())
stack = deque(i for i in range(N, 0, -1))

while len(stack) != 1:
    stack.pop()
    stack.appendleft(stack.pop())

print(stack[0])
