'''
1 - 모든 배열을 돌며 조건에 맞는 값을 새 배열에 담기
'''

def solution(arr, divisor):
    result = []
    for element in sorted(arr):
        if element % divisor == 0:
            result.append(element)
    
    if not result:
        result.append(-1)

    return result
