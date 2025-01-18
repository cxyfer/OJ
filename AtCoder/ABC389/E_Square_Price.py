"""
購買 k 件商品的價格為 k^2，故購買第 j 件商品的價格為 j^2 - (j-1)^2 = 2j-1，
故我們可以求得所有 N * 10^100 件商品的價格，
但顯然不可能列舉出所有商品的價格，而維護一個大小為 N 的堆也是不可行的。

因此考慮二分，找到一個整數 x，使得我們可以購買所有價格不超過 x 的商品。
對於價格為 p 的商品，若購買 k 件，則需滿足 (2k-1)*p <= x ，此時總價格為 p*k^2

二分找到最大的 x 後，由於此時可能還可以購買部分價格為 x+1 的商品，因此先用 x+1 計算總價格，
若總價格超過 M，則代表超過部分的商品價格都是 x + 1，
此時將超過的商品數量減去，即可得到答案。
"""
from math import *

N, M = map(int, input().split())
P = list(map(int, input().split()))

# 檢查當購買所有價格 <= x 的商品時，總價格會不會超過 M
def check(x):
    cost = 0
    for p in P:
        # (2 * k - 1) * p <= x
        k = (x + p) // (2 * p)
        cost += k * k * p
    return cost <= M

left, right = 0, 1 << 60
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1

x = right
ans = cost = 0
for p in P:
    # 改成盡可能購買價格為 x+1 的商品
    k = ((x + 1) + p) // (2 * p)
    cost += k * k * p
    ans += k

# 已知買所有價格 <= x 的商品，總價格不會超過 M，
# 但若買價格為 x+1 的商品，總價格會超過 M，則代表超過的商品價格都是 x + 1
more = cost - M
ans -= ceil(more / (x + 1))
print(ans)