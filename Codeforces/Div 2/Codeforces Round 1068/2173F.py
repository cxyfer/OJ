import math
from bisect import bisect_left
from itertools import accumulate

def solve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n
    
    # 根據複雜度分析，選擇適當的 B 值
    B = int(math.sqrt(n / math.log2(n))) + 1 if n > 1 else 1

    s = list(accumulate(A, initial=0))
        
    for _ in range(q):
        l, r, x = map(int, input().split())
        l -= 1  # 0-based index [l, r)
        cnt = rem = 0
        ln = 1
        while l < r:
            # 剩餘長度不足 ln 或 剩餘總和不足 x
            if r - l < ln or s[r] - s[l] < x:
                rem = s[r] - s[l]
                break
            
            # 1. 當前長度 ln 足夠
            if s[l + ln] - s[l] >= x:
                # ln >= B 時，直接跳躍
                if ln >= B:
                    while l + ln <= r and s[l + ln] - s[l] >= x:
                        l += ln
                        cnt += 1
                # ln < B 時，二分搜尋找到最大的跳躍次數
                else:
                    left, right = 1, (r - l) // ln
                    while left <= right:
                        mid = (left + right) // 2
                        if s[l + mid * ln] - s[l + (mid - 1) * ln] >= x:
                            left = mid + 1
                        else:
                            right = mid - 1
                    cnt += right
                    l += right * ln
                ln += 1
            #2. 嘗試 ln + 1
            elif l + ln + 1 <= r and s[l + ln + 1] - s[l] >= x:
                ln += 1
            # 3. 嘗試 ln + 2
            elif l + ln + 2 <= r and s[l + ln + 2] - s[l] >= x:
                ln += 2
            # 4. 二分搜尋找新的長度
            else:
                # 尋找最小的 idx 使得 s[idx] - s[l] >= x 即 s[idx] >= s[l] + x
                target = s[l] + x
                idx = bisect_left(s, target, lo=l + 1, hi=r + 1)
                
                cnt += 1
                ln = idx - l
                l = idx
        print(cnt, rem)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()

# N = Q = int(1.5e5)
# B = math.isqrt(N // int(math.log2(N))) + 1
# print(B)
# print(Q * B * math.log2(N) + N / B)


# B = math.isqrt(N * int(math.log2(N))) + 1
# print(B)
# print(Q * B + Q * N / B * math.log2(N))
# print(Q * (math.sqrt(int(N * math.log2(N))) + math.sqrt(N / math.log2(N))))
"""
在找新的 ln 時，最壞情況是每次都需要二分搜尋，設二分搜尋次數為 k，則：
ln = 1, 4, 7, ..., 1+3*(k-1)
sum(ln) <= N
(1 + 1 + 3k - 3) * k / 2 <= N
3k^2 - k - 2N <= 0
粗暴估計 k <= sqrt(2N/3) (實際解得 k <= (1 + sqrt(1 + 24N)) / 6)

此部分的時間複雜度為 O(Q * sqrt(2N/3) * log(N)) 約 8.15e8

在跳躍時，當 ln < B 時需要二分搜尋，當 ln >= B 時直接跳躍，則
Q * (B * log N + N / B)
找出一個 B 使得 B * log N + N / B 最小
當 B * log N = N / B 時，B * log N + N / B 最小，即 B = sqrt(N / log N)

此部分的時間複雜度為 O(Q * (sqrt(N * log N) + sqrt(N / log N)))
這部分需要 2.5e9 次運算
"""