#
# @lc app=leetcode id=3567 lang=python3
#
# [3567] Minimum Absolute Difference in Sliding Submatrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[float('inf')] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                arr = []
                for row in grid[i:i+k]:
                    arr.extend(row[j:j+k])
                arr.sort()
                for x, y in pairwise(arr):
                    if x != y:
                        ans[i][j] = min(ans[i][j], abs(x - y))
                if ans[i][j] == float('inf'):
                    ans[i][j] = 0
        return ans

from sortedcontainers import SortedList

class Solution2:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for u in range(m - k + 1):  # 枚舉上邊界
            cnt = defaultdict(int)
            sl = SortedList()  # 有序列表維護當前窗口內的元素
            hp = []  # 懶刪除堆維護最小的 (gap, a, b) 其中 a 和 b 是排序後相鄰的元素

            def is_valid(a: int, b: int) -> bool:  # 判斷 a 和 b 是否在 sl 中相鄰
                idx = sl.bisect_left(a)
                return idx + 1 < len(sl) and sl[idx] == a and sl[idx + 1] == b

            for right in range(n):
                # 1. 入窗口
                for i in range(u, u + k):
                    x = grid[i][right]
                    cnt[x] += 1
                    if cnt[x] > 1:
                        continue
                    # 插入新值，會新增兩組 gap 到堆中
                    sl.add(x)
                    idx = sl.bisect_left(x)
                    if idx > 0:
                        pre = sl[idx - 1]
                        heappush(hp, (x - pre, pre, x))
                    if idx + 1 < len(sl):
                        nxt = sl[idx + 1]
                        heappush(hp, (nxt - x, x, nxt))
                if right < k - 1:
                    continue
                # 2. 更新答案
                if len(sl) >= 2:
                    # 懶刪除堆，刪除不在 sl 中的 gap
                    while not is_valid(hp[0][1], hp[0][2]):
                        heappop(hp)
                    ans[u][right - k + 1] = hp[0][0]
                # 3. 出窗口
                for i in range(u, u + k):
                    y = grid[i][right - k + 1]
                    cnt[y] -= 1
                    if cnt[y] > 0:
                        continue
                    # 刪除舊值，會新增一組 gap 到堆中
                    idx = sl.bisect_left(y)
                    if idx > 0 and idx + 1 < len(sl):
                        pre = sl[idx - 1]
                        nxt = sl[idx + 1]
                        heappush(hp, (nxt - pre, pre, nxt))
                    del cnt[y]
                    sl.remove(y)
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.minAbsDiff([[1,8],[3,-2]], 2)) # [[2]]
print(sol.minAbsDiff([[3,-1]], 1)) # [[0,0]]
print(sol.minAbsDiff([[1,-2,3],[2,3,5]], 2)) # 	[[1,2]]