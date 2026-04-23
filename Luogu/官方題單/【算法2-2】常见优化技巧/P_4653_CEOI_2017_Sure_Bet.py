"""
P4653 [CEOI 2017] Sure Bet
https://www.luogu.com.cn/problem/P4653
Greedy + Two Pointers

如果在 A 中選取 i 個元素，且這些元素的總和為 sa、在 B 中選取 j 個元素，且這些元素的總和為 sb，
則收益為 min(sa, sb) - i - j，我們希望最大化這個收益。

顯然當我們選取 k 個元素時，最好是最大的 k 個元素，因此可以先將 A 和 B 分別由大到小排序。
注意 A 和 B 的同組元素實際上是沒有關聯的，因此可以分別處理。

接著由於 min(sa, sb) 的值取決於 sa 和 sb 較小值，因此可以在對較小的一方增加元素，
這可以使用雙指標(Two Pointers)來實現。

但需要注意當 j == n 時如果 sa < sb，則繼續增加 i 仍有可能得到更大的收益，反之同理。
"""


def solve():
    n = int(input())
    A = [0] * n
    B = [0] * n
    for i in range(n):
        A[i], B[i] = map(float, input().split())

    A.sort(reverse=True)
    B.sort(reverse=True)

    ans = 0
    sa = sb = 0
    i = j = 0
    # 只要目前較小的一側還能繼續補，就還可能讓答案變大
    while (i < n and sa <= sb) or (j < n and sa > sb):
        # 補目前總和較小的一側；補較大的一側只會增加成本
        if sa <= sb:
            sa += A[i]
            i += 1
        else:
            sb += B[j]
            j += 1
        ans = max(ans, min(sa, sb) - i - j)
    print(f"{ans:.4f}")


if __name__ == "__main__":
    solve()
