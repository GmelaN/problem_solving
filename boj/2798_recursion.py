from sys import stdin

def search(idx, count, psum, idxes):
    global nearest

    if count == 3:
        if nearest < psum <= M:
            nearest = psum
        return

    if idx == N:
        return
    
    search(idx + 1, count + 1, psum + cards[idx], idxes + [idx])
    search(idx + 1, count, psum, idxes)


N, M = map(int, stdin.readline().split())
cards = tuple(int(i) for i in stdin.readline().split())
nearest = 0

for i in range(N):
    search(i, 0, 0, [])

print(nearest)
