from itertools import accumulate

"""
Prefix sum
"""
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    pre = list(accumulate(A, initial=0)) # prefix sum

    ans = 0
    for k in range(1, N // 2 + 1): # 枚舉每輛卡車裝的箱子數量 k 
        if N % k == 0:
            mx = -float('inf')
            mn = float('inf')
            for j in range(k, N + 1, k):
                mx = max(mx, pre[j] - pre[j - k]) # 單一卡車上最大重量
                mn = min(mn, pre[j] - pre[j - k]) # 單一卡車上最小重量
            ans = max(ans, mx - mn) # 找出最大的差值
    print(ans)