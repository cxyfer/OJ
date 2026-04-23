"""
P3467 [POI 2008] PLA-Postering
https://www.luogu.com.cn/problem/P3467
Monotonic Stack

存在一種 n 的貼海報方案，即讓每棟建築都貼一張海報。
接著考慮要如何節省海報，可以發現當兩棟建築的高度相同，且中間沒有高度低於他們的建築時，
可以將兩棟建築的海報透過中間的建築合併成一張海報。

那麼對於 h[i] 我們只要維護左側第一個 <= h[i] 的位置，如果該位置的高度也為 h[i]，則可以節省一張海報。
這可以用 Monotonic Stack 解決。
"""


def solve():
    n = int(input())
    items = [tuple(map(int, input().split())) for _ in range(n)]

    ans = n
    st = []  # 維護高度非遞減的堆疊
    for _, h in items:
        while st and st[-1] > h:
            st.pop()
        if st and st[-1] == h:
            ans -= 1
        st.append(h)
    print(ans)


if __name__ == "__main__":
    solve()
