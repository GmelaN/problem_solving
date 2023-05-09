from sys import stdin

N, M = map(int, stdin.readline().split())
cards = tuple(int(i) for i in stdin.readline().split())
nearest = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            psum = cards[i] + cards[j] + cards[k]

            if nearest < psum <= M:
                nearest = psum

print(nearest)
