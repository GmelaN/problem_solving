from sys import stdin

N = int(stdin.readline())
eval_ = stdin.readline().rstrip()
operands = [int(stdin.readline()) for i in range(N)]

stack = []

for i in eval_:
    if i.isalpha():
        stack.append(operands[ord(i) - ord('A')])
    
    else:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            tmp = stack.pop()
            if i == '/':
                stack.append(stack.pop() / tmp)
            else:
                stack.append(stack.pop() - tmp)

print("%.2f" % (stack[0]))



