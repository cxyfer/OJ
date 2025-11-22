"""
構造
gcd(a, b) > 1 代表 spf[a] == spf[b]
因此可以將所有數字按照 spf 分組，然後構造答案。

對於相同的 spf 值 x，可以構造如下的答案：
_, x, x, _, x, x, _, x, x, ...
多段拼接時形如：
_, x, x, _, x, x, y, y, _, y, y, z, z, _, z, z, ...

正確性不會證，但只要 n 夠大應該是可以幾乎拚完的。
"""
import math
from collections import defaultdict

MAX_N = int(2e5 + 5)
primes = []
spf = list(range(MAX_N))
for i in range(2, math.isqrt(MAX_N) + 1):
    if spf[i] == i:
        primes.append(i)
        for j in range(i * i, MAX_N, i):
            spf[j] = min(spf[j], i)

def solve():
    n = int(input())
        
    groups = defaultdict(list)
    for i in range(1, n + 1):
        groups[spf[i]].append(i)

    ans = [-1] * n
    idx = 1
    rem = []
    for p, lst in groups.items():
        m = len(lst)
        if m == 1:
            rem.extend(lst)
            continue
        for j in range(0, m - 1, 2):
            if idx + 1 < n:
                ans[idx] = lst[j]
                ans[idx + 1] = lst[j + 1]
                idx += 3
            else:
                rem.extend(lst[j:])
                break
        else:
            idx -= 1
            if m & 1:
                rem.append(lst[-1])

    idx = 0
    for x in rem:
        while ans[idx] != -1:
            idx += 1
        ans[idx] = x
    
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()