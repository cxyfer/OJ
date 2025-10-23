"""
C - 数列之和
https://ac.nowcoder.com/acm/contest/95338/C

ai = 2 * i
令 s(l, r) 表示 [l, r] 區間內的元素之和，根據等差數列求和公式，有：
s(l, r) = (r - l + 1) * (2 * l + 2 * r) / 2 = (r - l + 1) * (l + r)
其中 (r - l + 1) 和 (l + r) 必為一奇數和一偶數，故 s(l, r) 的結果為偶數。

如果奇數為 1 ，顯然 s(l, r) 可以表示所有偶數，
但由於題目規定 (r - l + 1) >= 2，故只有當 (l, r) = (0, 1) 時，奇數才能為 1。
而在所有偶數中，除了 2^p 外，皆可以表示為 2 * x 的形式，其中 x 為 > 1 的奇數。
唯一的例外是當 (l, r) = (0, 1) 時，s(l, r) = 2。

故 s(l, r) 可以表示除了 2^p (p > 1)外的所有偶數。
這個結論也能透過打表發現。

實作時枚舉缺失的數字數量 r，使得 r 滿足：
2^(r + 1) <= 2 * (k + r) < 2^(r + 2)
"""

def solve():
    k = int(input())
    for r in range(70):
        if (1 << r) <= k + r < (1 << (r + 1)):
            print(2 * (k + r))
            break

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()