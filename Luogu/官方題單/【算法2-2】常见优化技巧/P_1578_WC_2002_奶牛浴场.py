"""
P1578 [WC2002] 奶牛浴场
https://www.luogu.com.cn/problem/P1578

觀察到：最大矩形至少有一條邊是緊貼障礙點或邊界的，以下稱其為 tight edge。
我們可以將四個角落點也視為障礙點，這樣就不用特別處理邊界情況。
接著枚舉 tight edge 上的其中一個點作為基準點。
固定基準點後，只需要往一個方向掃描，同時用兩個變數 lo、hi 動態維護另一個維度的合法範圍即可。
但 tight edge 可能是垂直的，也可能是水平的，所以要分別處理垂直方向（左→右）和水平方向（下→上） 兩種情況。
每次掃描時「先更新答案，再把當前點加入限制」非常關鍵，因為點允許出現在邊界上。

為什麼兩個方向就足夠？
因為任意最大空矩形一定至少有一條 tight edge，而 tight edge 只可能是以下四種之一：
1. 左邊界 tight → 第一趟（左→右）一定能抓到（固定那個 tight 點作為 x1）
2. 右邊界 tight → 第一趟在掃描過程中，當 x2 是那個 tight 點時，先算面積再更新的機制會捕捉到
3. 下邊界 tight → 第二趟（下→上）一定能抓到，同左邊界情況
4. 上邊界 tight → 第二趟同樣能透過先算面積的時機捕捉到，同右邊界情況

有一種情況是當 x1 = x2 時，此時限制垂直方向上的上邊界或下邊界似乎會有差異，但這種情況在垂直方向從下往上掃描時就能被解決。

當然為了保險起見，四個方向都掃描一遍也是可以的。
"""


def solve():
    L, W = map(int, input().split())
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    points.extend([(0, 0), (0, W), (L, 0), (L, W)])
    n += 4

    def calc(points: list[tuple[int, int]], U: int) -> int:
        points.sort(key=lambda p: (p[0], p[1]))
        ans = 0
        for i, (x1, y1) in enumerate(points):
            lo, hi = 0, U
            for j in range(i + 1, n):
                x2, y2 = points[j]
                ans = max(ans, (x2 - x1) * (hi - lo))
                if y2 < y1:
                    lo = max(lo, y2)
                else:
                    hi = min(hi, y2)
        return ans

    ans1 = calc(points, W)  # 由左到右
    ans2 = calc([(y, x) for x, y in points], L)  # 由下到上
    print(max(ans1, ans2))


if __name__ == "__main__":
    solve()
