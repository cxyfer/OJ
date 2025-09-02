N = int(input())

A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]

ans = (0, 0)
for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            ans = (i+1, j+1)
print(*ans)