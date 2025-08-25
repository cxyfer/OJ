"""
2044E. Insane Problem
題意：計算有多少 (x, y) 滿足 l1 <= x <= r1 以及 l2 <= y <= r2 且 y / x = k^n

枚舉 k^n 的值，k^n 最大為 r2，因此最多枚舉 log(r2) 次
由於 x = y / k^n，因此可以對 l2 <= y <= r2 同除 k^n 得到 l2 / k^n <= x <= r2 / k^n
此時可以將對 y 的限制轉換為對 x 的限制，對於每個 k^n，計算有多少 x 滿足條件即可。

時間複雜度：O(log(r2))
"""
import math

def solve():
    k, l1, r1, l2, r2 = map(int, input().split())

    ans = 0
    kn = 1
    while kn <= r2:
        lo = max(l1, math.ceil(l2 / kn))
        hi = min(r1, math.floor(r2 / kn))
        ans += max(hi - lo + 1, 0)
        kn *= k
    print(ans)

t = int(input())
for _ in range(t):
    solve()