T = int(input())

def check(x, y, c):
    if x < 0 or y < 0 or x >= M or y >= N:
        return False
    for i in range(-c, c+1):
        for j in range(-c, c+1):
            if x+i < 0 or y+j < 0 or x+i >= M or y+j >= N:
                return False
            if mp[x+i][y+j] != mp[x][y]:
                return False
    return True

for _ in range(T):
    M, N, Q = map(int, input().split())
    mp = [list(input()) for _ in range(M)]
    print(M, N, Q)
    for _ in range(Q):
        qx, qy = map(int, input().split())
        c = 0
        while check(qx, qy, c):
            c += 1
        print(2*c-1)