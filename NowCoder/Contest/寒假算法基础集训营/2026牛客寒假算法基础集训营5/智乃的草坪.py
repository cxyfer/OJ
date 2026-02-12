"""
C. 智乃的草坪
https://ac.nowcoder.com/acm/contest/120565/C

若經過 t 秒能完整覆蓋草坪，則 > t 秒也一定能完整覆蓋草坪，因此可以對時間 t 進行二分搜尋。

接著考慮如何判斷經過 t 秒後，是否可以完整覆蓋草坪。
因為灑水器位於 x 軸上，且草坪的範圍對 x 軸對稱，所以只需要考慮 x 軸上的部分即可。
做圖後可以發現，若經過一定時間 t 後，灑水器可以和 y = r 交於兩個點，令其分別為 (x1, r) 和 (x2, r)，其中 x1 < x2。
則這個灑水器可以覆蓋 [x1, x2] 這個區間。

因此對於固定的時間 t，可以轉換為區間覆蓋問題，問是否可以選擇 <= k 個區間，使得這些區間可以覆蓋 [0, c] 這個區間。
可以貪心的方式解決，依照左端點排序後，維護目前已經包含的區間右端點，每次從已包含的區間中選擇右端點最大的區間擴增。

另外由於題目保證所有灑水器都在 [0, c] 這個區間內，且 r >= 1，因此最多 max(c, 2r) 秒就可以完整覆蓋草坪。
"""
import math

def solve():
    n, k, r, c = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]

    def check(t):
        intervals = []
        for p, v in items:
            ri = v * t
            if ri < r:
                continue
            d = math.sqrt(ri * ri - r * r)

            # C++ 可以把全部區間丟去排序，然而 Python 會 TLE，需要去除無效區間
            # intervals.append((p - d, p + d))

            # 然而這樣寫在二分區間為 [0, 1e9] (二分次數約為 45 次) 時會 TLE 
            # 需要改成正確的二分區間 [0, 2e6] (二分次數約為 35 次)
            # li, ri = p - d, p + d
            # if ri >= 0 and li <= c:
            #     intervals.append((li, ri))

            # 這樣寫的常數似乎比較小，二分區間為 [0, 1e9] 時不會 TLE
            li = max(0, p - d)
            ri = min(c, p + d)
            if li <= ri:
                intervals.append((li, ri))

        if not intervals:
            return False
        
        m = len(intervals)
        intervals.sort(key=lambda x: x[0])
 
        i = cnt = 0
        cur = 0.0  # 目前已經包含的區間右端點
        while cur < c and cnt < k and i < m:
            nxt = float('-inf')  # 下次可以擴增到的右端點
            while i < m and intervals[i][0] <= cur:
                if intervals[i][1] > nxt:
                    nxt = intervals[i][1]
                i += 1
            if nxt <= cur:
                return False
            cur = nxt
            cnt += 1
        return cur >= c
    
    left, right = 0, max(c, 2 * r)
    while right - left > 1e-4:
        mid = (left + right) / 2
        if check(mid):
            right = mid
        else:
            left = mid
    print(f"{right:.10f}")

if __name__ == '__main__':
    solve()