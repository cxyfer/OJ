"""
P1091 [NOIP 2004 提高组] 合唱队形
https://www.luogu.com.cn/problem/P1091

Same as:
- LC1671. Minimum Number of Removals to Make Mountain Array
"""
from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

def getLIS(A: list[int]) -> list[int]:
    res = []
    f = []
    for x in A:
        idx = bisect_left(f, x)
        if idx == len(f):
            f.append(x)
        else:
            f[idx] = x
        res.append(idx + 1)
    return res

pre = getLIS(A)
suf = getLIS(A[::-1])[::-1]
ans = 0
for i in range(n):
    ans = max(ans, pre[i] + suf[i] - 1)
print(n - ans)