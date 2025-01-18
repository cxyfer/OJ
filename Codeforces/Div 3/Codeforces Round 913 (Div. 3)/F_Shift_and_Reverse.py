def rotate(A: list) -> int: # 檢查能否透過右移 k 次，使A變成遞增或遞減，的最小 k 值
    """
        直接枚舉右移 k 次，複雜度 O(N^2)，會TLE
        改為檢查有沒有連續 N 個數字遞增或遞減，複雜度 O(N)
    """
    res = float('inf')
    cnt = 1
    for i in range(2*N-2, -1, -1): # 遞增的情況
        if A[i % N] <= A[(i+1) % N]:
            cnt += 1
        else:
            cnt = 1
        if cnt == N:
            res = min(res, N-i)
            break

    cnt = 1
    for i in range(2*N-2, -1, -1): # 遞減的情況
        if A[i % N] >= A[(i+1) % N]:
            cnt += 1
        else:
            cnt = 1
        if cnt == N:
            res = min(res, N-i+1) # 遞減，需要多一次反轉
            break
    return res

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    if N == 1: # 要特判N=1的情況
        print(0)
        continue

    res1 = rotate(A)
    res2 = rotate(A[::-1]) + 1 # 反轉算一次操作次數
    ans = min(res1, res2)
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

