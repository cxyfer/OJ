"""
C. Inverted World
https://ac.nowcoder.com/acm/contest/120563/C

DP

最終只會有以0開頭或以1開頭的01交錯字串，分別計算兩種情況所需的代價即可。

接著考慮如何計算代價：
顯然僅需考慮與預期不符的位置，與預期相同的位置不需要修改，額外加入這些多餘的位置代價是不降的。
也就是說，對於與預期不符的位置，我們需要將其劃分成若干個子序列，且每個子序列都是 01 交錯的。

可以維護 cnt0 和 cnt1 分別表示當前以 0/1 結尾的子序列數量，
那麼當遇到與預期不符的位置時，可以將其劃分成一個新的子序列，或者加入到當前以 0/1 結尾的子序列中。
"""
def solve():
    n = int(input())
    s = input()
    assert len(s) == n

    def helper(b: int) -> int:
        res = cnt0 = cnt1 = 0
        for i, ch in enumerate(s):
            if ch == str((i + b) & 1):
                continue
            if ch == '0':
                if cnt1 > 0:
                    cnt1 -= 1
                else:
                    res += 1
                cnt0 += 1
            else:
                if cnt0 > 0:
                    cnt0 -= 1
                else:
                    res += 1
                cnt1 += 1
        return res
        
    print(min(helper(0), helper(1)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()