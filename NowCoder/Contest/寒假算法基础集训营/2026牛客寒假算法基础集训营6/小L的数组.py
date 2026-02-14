"""
H. 小L的数组
https://ac.nowcoder.com/acm/contest/120566/H

可達性 DP
令 f[i][v] 表示使用前 i 個元素，是否可以得到值 v，初始化 f[0][0] = True
用刷表法，對每個元素，更新其可達的值：
- f[i][max(0, v - A[i])] <- f[i - 1][v]
- f[i][v ^ B[i]] <- f[i - 1][v]

由於 v 的範圍是 2^11，且兩種操作都不會改變值域，因此可以用 set 或 bitmask 維護即可。
"""


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert len(A) == len(B) == n

    # 使用 set 維護
    # f = set([0])
    # for a, b in zip(A, B):
    #     nf = set()
    #     for x in f:
    #         nf.add(max(0, x - a))
    #         nf.add(x ^ b)
    #     f = nf
    # print(max(f))

    # 使用 bitmask 維護
    f = 1
    for a, b in zip(A, B):
        nf = 0
        while f:
            lb = f & -f
            f &= ~lb
            v = lb.bit_length() - 1
            nf |= 1 << max(0, v - a)
            nf |= 1 << (v ^ b)
        f = nf
    print(f.bit_length() - 1)


if __name__ == "__main__":
    solve()
