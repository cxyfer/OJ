"""
構造 + Meet in the Middle 

操作次數最多為 2n 次，這暗示我們不直接把 s 轉換為 t，而是將兩者轉換為相同字串後再進行反向操作。
注意到連續段一定是迴文的，故可以對連續段進行操作，操作後又可以與其鄰居合併，形成新的連續段。
但只有一種情況會導致沒有連續段，也就是 1010... 或 0101... 的交錯排列型態。
這時前 3 個字元也必定是迴文的，故可以對前 3 個字元進行操作，操作後又可以與其鄰居合併，形成新的連續段。

由於每次至少可以讓連續段的長度 + 1，因此最多需要 n - 1 次就能得到一個連續段，如果得到的是 1 的話則需要再進行 1 次操作，總共需要 n 次操作。
"""
from itertools import pairwise

def calc(s):
    n = len(s)
    ans = []
    while sum(s) > 0:
        l, r = 0, 2
        for i, (x, y) in enumerate(pairwise(s)):
            if x == y:
                l, r = i, i + 1
                while r < n - 1 and s[r + 1] == x:
                    r += 1
                break
        ans.append((l + 1, r + 1))
        for k in range(l, r + 1):
            s[k] ^= 1
    return ans

def solve():
    n = int(input())
    s = list(map(int, input()))
    t = list(map(int, input()))
    assert n == len(s) == len(t)

    ans = calc(s) + calc(t)[::-1]
    print(len(ans))
    for l, r in ans:
        print(l, r)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()