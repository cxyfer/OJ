"""
A. 本场比赛灵感来源于树状数组出题组
https://ac.nowcoder.com/acm/contest/120564/A

排序 + 二分
排序後二分查找有多少個元素 <= x，注意需要去除自身，所以需要 -1
如果 >= 0.8(n - 1)，則累加 x
"""
from math import ceil
from bisect import bisect_right

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    A.sort()
    m = ceil((n - 1) * 0.8)
    ans = 0
    for x in A:
        if bisect_right(A, x) - 1 >= m:
            ans += x
    print(ans)

if __name__ == "__main__":
    solve()