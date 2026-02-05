"""
B. NCPC
https://ac.nowcoder.com/acm/contest/120562/B

賽時一開始沒讀清楚題，以為存活的人必須參與最後一次比賽，
然而其實可以讓別人自相殘殺，最後漁翁得利。

所以可以利用最大值消除其他對手，並使最大值兩兩捉對廝殺，最後讓我們想要的目標存活。
- 如果最大值的數量為偶數，則可以讓除了最大值之外的任何人成為存活者
- 如果最大值的數量為奇數，則只有最大值可以成為存活者
"""
from collections import Counter

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    cnt = Counter(A)
    mx = max(A)

    ans = ['0'] * n
    if cnt[mx] & 1:
        for i, x in enumerate(A):
            if x == mx:
                ans[i] = '1'
    else:
        for i, x in enumerate(A):
            if x < mx:
                ans[i] = '1'

    print(*ans, sep='')

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()