from sys import stdin

def search(idx, p_array):
    global ARRAY, visited

    if len(p_array) == M:
        for i in p_array:
            print(i, end=' ')
        print("")
        return

    if idx == N:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            search(i, p_array + [ARRAY[i]])
            visited[i] = False

N, M = map(int, stdin.readline().split())
ARRAY = tuple(i for i in range(1, N + 1))
visited = [False for _ in range(N + 1)]

search(0, [])
