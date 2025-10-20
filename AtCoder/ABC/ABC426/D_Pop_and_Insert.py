"""
貪心 (Greedy)

考慮全部修改為 0 或全部修改為 1 兩種情況。
在操作後最終會有一段連續的 0 或 1 不用操作，
剩下部分若與修改後的結果相反，則需要操作 1 次；與修改後的結果相同，則需要操作 2 次。
為使操作次數最小，可以選取最長的連續 0 或 1 段保留，操作其他部分。
"""

from itertools import groupby


def solve():
    _ = int(input())
    S = input()

    cnt = [0] * 2
    mx = [0] * 2
    for ch, lst in groupby(S):
        ch = ord(ch) - ord('0')
        sz = len(list(lst))
        cnt[ch] += sz
        mx[ch] = max(mx[ch], sz)

    ans = min(
        (cnt[0] - mx[0]) * 2 + cnt[1],
        (cnt[1] - mx[1]) * 2 + cnt[0],
    )
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
