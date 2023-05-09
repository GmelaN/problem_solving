EMPTY = -1

def solution(n):
    answer = [[EMPTY for _ in range(n)] for _ in range(n)]

    content = 1
    i, j = 0, 0
    
    while content <= n*n:
        while j < n and answer[i][j] == EMPTY:
            answer[i][j] = content
            j += 1
            content += 1
        
        j -= 1
        i += 1

        while i < n and answer[i][j] == EMPTY:
            answer[i][j] = content
            i += 1
            content += 1
        
        i -= 1
        j -= 1

        while j >= 0 and answer[i][j] == EMPTY:
            answer[i][j] = content
            j -= 1
            content += 1
        
        j += 1
        i -= 1

        while i >= 0 and answer[i][j] == EMPTY:
            answer[i][j] = content
            i -= 1
            content += 1
        
        i += 1
        j += 1

    return answer


'''


'''
print(solution(4))