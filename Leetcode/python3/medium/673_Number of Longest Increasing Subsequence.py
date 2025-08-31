#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
BIT 優化 DP 求最長的 LIS 及其數量
"""
# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        mp = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
        sz = len(mp)

        # BIT
        tree = [[0, 0] for _ in range(sz + 1)]
        def update(k: int, mx: int, cnt: int) -> None:
            while k < len(tree):
                # tree[k] += x
                if mx > tree[k][0]:
                    tree[k] = [mx, cnt]
                elif mx == tree[k][0]:
                    tree[k][1] += cnt
                k += (k & -k)

        def query(k: int) -> int:
            res = [0, 0]
            while k > 0:
                # res += tree[k]
                if tree[k][0] > res[0]:
                    res = tree[k][:]
                elif tree[k][0] == res[0]:
                    res[1] += tree[k][1]
                k -= (k & -k)
            return res
        
        # 求 LIS 數量
        for v in nums:
            # update(mp[v], 1 + query(mp[v] - 1))
            mx, cnt = query(mp[v] - 1)
            update(mp[v], mx + 1, max(cnt, 1))
        return query(sz)[1]
# @lc code=end

