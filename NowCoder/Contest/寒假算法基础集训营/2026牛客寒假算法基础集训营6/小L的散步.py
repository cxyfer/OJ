"""
G. 小L的散步
https://ac.nowcoder.com/acm/contest/120566/G

前綴和 + 二分查找

對石塊的長度做前綴和，便可以得到每個縫隙的位置 pos
令我們當前走的距離為 s，則可以得到腳掌的區間 [s, s + l]
要判斷腳掌是否踩到縫隙，可以在 pos 上二分查找出第一個 > s 的位置 idx1，和第一個 < s + l 的位置 idx2
若 idx1 <= idx2，則表示腳掌的區間 [s, s + l] 內有縫隙
注意由於腳掌的邊緣可以踩到縫隙上，因此是 > s 和 < s + l
"""
from itertools import accumulate
from bisect import bisect_left, bisect_right


def solve():
    n, m, l = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert len(A) == n and len(B) == m

    pos = list(accumulate(A))

    s = 0
    for x in [0] + B:
        s += x
        idx1 = bisect_right(pos, s)
        idx2 = bisect_left(pos, s + l) - 1
        if idx1 <= idx2:
            print("YES")
            break
    else:
        print("NO")


if __name__ == "__main__":
    solve()
