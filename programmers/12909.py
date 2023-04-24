def solution_1(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(0)
        else:
            if not stack:
                return False
            stack.pop()
        
    return len(stack) == 0

def solution_2(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False

            count -= 1
        
    return count == 0