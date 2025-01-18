T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if K == 1:
        ans = 0 if A[0] % K == 0 else K - A[0] % K
        print(ans)
        continue

    ans = float('inf')
    cnt_o = cnt_e = 0
    for a in A:
        if a % 2 == 1:
            cnt_o += 1
        else:
            cnt_e += 1
        r = a % K
        if r == 0:
            ans = 0
            break
        ans = min(ans, K - r)
    
    if K == 4:
        if cnt_e >= 2: # 有兩個偶數
            ans = 0
        elif cnt_e >= 1: # 有一個偶數
            ans = min(ans, 1)
        else: # 全奇數
            ans = min(ans, 2)

    print(ans)
    
