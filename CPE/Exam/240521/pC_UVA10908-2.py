T = int(input())

def check(x, y, r):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    for i in range(-r, r + 1):
        for j in [-r, r]:
            if x + i < 0 or x + i >= M or y + j < 0 or y + j >= N:
                return False
            if mp[x + i][y + j] != mp[x][y]:
                return False
    for j in range(-r, r + 1):
        for i in [-r, r]:
            if x + i < 0 or x + i >= M or y + j < 0 or y + j >= N:
                return False
            if mp[x + i][y + j] != mp[x][y]:
                return False
    return True

for _ in range(T):
    M, N, Q = map(int, input().split())
    mp = [list(input()) for _ in range(M)]
    print(M, N, Q)
    for _ in range(Q):
        x, y = map(int, input().split())
        r = 1
        while check(x, y, r):
            r += 1
        print(2 * r - 1)