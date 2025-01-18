"""
    後綴和 + 貪心
"""

from itertools import accumulate

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    
    # 後綴和，suf[i] = sum(A[i:])
    suf = list(accumulate(A[::-1], initial=0))[::-1]

    # 考慮貢獻度
    ans = suf[0] # 貢獻度都至少為1
    for i in range(1, N):
        if suf[i] >= 0: # 為使結果盡量大，當 sum(A[i:]) >= 0，可以增加A[i:]的貢獻度，即 += suf[i]
            ans += suf[i]
    print(ans)
