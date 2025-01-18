T = int(input())

def check(A, M): # 滿足 A[i] | A[j] = M[i][j]
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if A[i] | A[j] != M[i][j]:
                return False
    return True

for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]

    A = [0] * N

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if (i==0 and j==1) or (i>=1 and j==0):
                A[i] = M[i][j]
            else:
                A[i] = A[i] & M[i][j]
    if check(A, M):
        print("YES")
        print(*A)
    else:
        print("NO")