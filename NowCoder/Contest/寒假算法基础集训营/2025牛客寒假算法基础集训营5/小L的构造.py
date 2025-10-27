"""
L - 小L的构造
https://ac.nowcoder.com/acm/contest/95337/L

構造 + 歐幾里得算法求 gcd

  1  2  3  4  5  6
  7  8  9 10 11 12
 13 14 15 16 17 18
 19 20 21 22 23 24
 25 26 27 28 29 30
 31 32 33 34 35 36

每六個數一組，令 x = 6k + 1，其中 k >= 0，
則 x + 2, x + 5 皆為 3 的倍數；x + 1, x + 3 皆為 2 的倍數。
可以分成 (x, x + 1, x + 3) 和 (x + 2, x + 4, x + 5) 兩組。
- (x, x + 1) 以及 (x + 4, x + 5) 由於相鄰故必定互質
- gcd(x, x + 3) = gcd(x, 3)，但 x 必定不是 3 的倍數，故 gcd(x, x + 3) = 1
- gcd(x + 2, x + 4) = gcd(x + 2, 2)，但 x + 2 必定是奇數，故 gcd(x + 2, x + 4) = 1
上述構造可以滿足 ans = 2t 的情況。
(1, 2, 4) (3, 5, 6)

對於 ans = 2t + 1 的情況，可以令 x = (6 * k) + 4
則 x + 2, x + 5 皆為 3 的倍數；x, x + 4 皆為 2 的倍數。
分成 (x, x + 3, x + 4) 和 (x + 1, x + 2, x + 5) 兩組。
- (x + 3, x + 4) 以及 (x + 1, x + 2) 由於相鄰故必定互質
- gcd(x, x + 3) = gcd(x, 3)，但 x 必定不是 3 的倍數，故 gcd(x, x + 3) = 1
- gcd(x + 1, x + 5) = gcd(x + 1, 4)，但 x + 1 必定是奇數，故 gcd(x + 1, x + 5) = 1
但此時會剩餘 (1, 2, 3) 無法構造，故需要調整。
透過暴力打表，可以將前 9 個數字分成 (1, 2, 4) (3, 5, 9) (6, 7, 8)
"""

from math import gcd
from itertools import combinations

def check(g):
    cnt = [0, 0]
    for c in combinations(g, 2):
        cnt[gcd(c[0], c[1]) > 1] += 1
    return cnt[0] == 2 and cnt[1] == 1

def solve():
    n = int(input())

    if n <= 3:
        print(0)
    elif n <= 5:
        print(1)
        print(1, 2, 4)
    else:
        p = n // 3
        print(p)
        ans = []
        if p & 1:
            ans.extend([(1, 2, 4), (3, 5, 9), (6, 7, 8)])
            for k in range(1, p // 2):
                ans.append((6 * k + 4, 6 * k + 7, 6 * k + 8))
                ans.append((6 * k + 5, 6 * k + 6, 6 * k + 9))
        else:
            for k in range(p // 2):

                ans.append((6 * k + 1, 6 * k + 2, 6 * k + 4))
                ans.append((6 * k + 3, 6 * k + 5, 6 * k + 6))
        # assert len(ans) == p
        # assert all(check(g) for g in ans)
        print(*[' '.join(map(str, g)) for g in ans], sep='\n')

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()