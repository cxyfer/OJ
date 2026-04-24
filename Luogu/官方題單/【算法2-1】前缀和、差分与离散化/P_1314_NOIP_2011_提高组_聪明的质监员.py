"""
P1314 [NOIP 2011 提高组] 聪明的质监员
https://www.luogu.com.cn/problem/P1314
二分 + 前綴和

對於固定的 W，我們可以用兩個前綴和分別處理區間內 >= W 的物品數量以及物品價值總和。
然後對於每個詢問，我們可以用這兩個前綴和在 O(1) 時間內計算出其質量檢驗值 val 。

而目標是使 |val - k| 最小，因此我們可以找到第一個 >= k 的 val 和最後一個 < k 的 val。
這可以用透過二分來實現，另外最後一個 < k 的 val 就是第一個 >= k 的 val - 1。
"""


def solve():
    n, m, k = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    queries = [tuple(map(int, input().split())) for _ in range(m)]

    s_cnt = [0] * (n + 1)
    s_sum = [0] * (n + 1)

    def check(W):
        for i, (w, v) in enumerate(items, start=1):
            s_cnt[i] = s_cnt[i - 1] + (1 if w >= W else 0)
            s_sum[i] = s_sum[i - 1] + (v if w >= W else 0)
        res = 0
        for l, r in queries:
            res += (s_cnt[r] - s_cnt[l - 1]) * (s_sum[r] - s_sum[l - 1])
        return res

    maxW = max(w for w, _ in items)
    left, right = 0, maxW
    while left <= right:
        mid = (left + right) // 2
        if check(mid) >= k:
            left = mid + 1
        else:
            right = mid - 1

    print(min(k - check(left), check(right) - k))


if __name__ == "__main__":
    solve()
