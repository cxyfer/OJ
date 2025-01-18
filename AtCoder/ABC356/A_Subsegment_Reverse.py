N, L, R = map(int, input().split())
for i in range(1, L): # [1, L)
    print(i, end=' ')
for i in range(R, L-1, -1): # [L, R]
    print(i, end=' ')
for i in range(R+1, N+1): # (R, N]
    print(i, end=' ' if i != N else '\n')