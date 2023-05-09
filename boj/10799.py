from sys import stdin

s = stdin.readline().rstrip()
stack = []

count = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(0)
    else:
        stack.pop()

        if s[i-1] == '(': # 직전이 레이저인 경우
            count += len(stack)
        else:
            count += 1

print(count)
