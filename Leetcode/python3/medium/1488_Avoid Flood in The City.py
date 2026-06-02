#
# @lc app=leetcode id=1488 lang=python3
#
# [1488] Avoid Flood in The City
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 有序容器上二分
2. 區間併查集
"""
# @lc code=start
class Solution1:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        ans = [1] * n
        mp = dict()  # x -> last_rain
        sl = SortedList()  # 有序容器維護可用的位置
        for i, x in enumerate(rains):
            if x == 0:
                sl.add(i)
            else:
                if x in mp:
                    # 需要先清掉積水
                    idx = sl.bisect_right(mp[x])
                    if idx == len(sl):  # 沒有可用的位置
                        return []
                    ans[sl.pop(idx)] = x
                mp[x] = i
                ans[i] = -1
        return ans


class Solution2:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        ans = [1] * n
        mp = dict()  # x -> last_rain

        # 區間並查集維護可用的位置
        # fa[i] = j 表示從位置 i 開始，下一個可用的位置是 j
        fa = list(range(n + 1))  # 注意要 +1，因為可能會 union(n - 1, n)

        def find(x: int) -> int:
            while x != fa[x]:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x
            
        def union(x: int, y: int) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            fa[x] = fy
            return True
        
        for i, x in enumerate(rains):
            if x > 0:
                if x in mp:
                    # 需要先清掉積水
                    j = find(mp[x])
                    if j >= i:
                        return []
                    ans[j] = x
                    union(j, j + 1)  # 將 j 標記為不可用
                mp[x] = i
                ans[i] = -1
                union(i, i + 1)  # 將 i 標記為不可用
        return ans


Solution = Solution1
# Solution = Solution2
# @lc code=end

