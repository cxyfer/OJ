"""
    r <= sqrt(x^2 + y^2) < r+1
    r^2 <= x^2 + y^2 < (r+1)^2 => r^2 <= x^2 + y^2 <= (r+1)^2 - 1
    sqrt(r^2 - x^2) <= y <= sqrt((r+1)^2 - 1 - x^2)

    枚舉 x 座標，計算 y 座標的範圍，然後計算 y 座標的個數。
    由於要考慮負數，所以要將 y 座標的範圍乘以 2，最後再減去 y 座標下界為 0 的情況。
"""
from math import *

t = int(input())

for _ in range(t):
    r = int(input())
    ans = 0
    for x in range(-r, r+1): # 枚舉 x 座標
        v1 = ceil(sqrt(r**2 - x**2)) # y 座標的下界
        v2 = floor(sqrt((r+1)**2 - 1 - x**2))
        ans += 2 * (v2 - v1 + 1) - (v1 == 0)
    print(ans)