#
# @lc app=leetcode id=3486 lang=python3
#
# [3486] Longest Special Path II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        ans = (-1, 0)
        s = [0]  # prefix sum
        mp = defaultdict(lambda: [-1, -1])  # depth list of each color
        def dfs(u: int, fa: int, d: int, top: int, pre: int) -> None:
            """
                u: 當前節點
                fa: 父節點
                d: 當前深度，即窗口的右端點
                top: 當前窗口內最小的深度，即窗口的左端點
                pre: 當前窗口內上一個出現兩次的顏色
            """
            nonlocal ans

            x = nums[u]  # color
            top = max(top, mp[x][-2] + 1)

            if mp[x][-1] != -1:  # 有兩個 x
                # 根據上一個多出來的 pre 和 x 的深度，決定刪哪個
                top = max(top, min(mp[pre][-2], mp[x][-1]) + 1)
                pre = x if (mp[pre][-2] < mp[x][-1]) else pre

            ans = max(ans, (s[d] - s[top], -(d - top + 1)))

            mp[x].append(d)
            for v, w in g[u]:
                if v == fa:
                    continue
                s.append(s[-1] + w)
                dfs(v, u, d + 1, top, pre)
                s.pop()
            mp[x].pop()

        dfs(0, -1, 0, 0, -1)
        return [ans[0], -ans[1]]
# @lc code=end

sol = Solution()

edges = [[0,1,1],[1,2,3],[1,3,1],[2,4,6],[4,7,2],[3,5,2],[3,6,5],[6,8,3]]
nums = [1,1,0,3,1,2,1,1,0]
print(sol.longestSpecialPath(edges, nums))  # [9,3]

edges = [[1,0,3],[0,2,4],[0,3,5]]
nums = [1,1,0,2]
print(sol.longestSpecialPath(edges, nums))  # [5,2]

edges = [[0,2,4],[1,2,10],[3,1,5]]
nums = [4,5,4,5]
print(sol.longestSpecialPath(edges, nums))  # [15,3]

edges = [[2,1,7],[0,3,10],[4,0,3],[1,5,5],[4,1,5],[4,6,1]]
nums = [2,4,2,2,4,4,1]
print(sol.longestSpecialPath(edges, nums))  # [12,3]

edges = [[8,0,3],[5,1,6],[6,2,8],[4,7,5],[4,2,4],[5,2,2],[5,3,10],[8,3,9]]
nums = [2,2,5,3,4,2,4,4,3]
print(sol.longestSpecialPath(edges, nums))  # [29,5]