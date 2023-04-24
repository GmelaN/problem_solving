from math import ceil
def solution(n):
    if n == 1:
        return "수"

    answer = "수박" * ceil(n / 2)

    if n % 2 != 0:
        answer = answer[:-1]

    return answer
