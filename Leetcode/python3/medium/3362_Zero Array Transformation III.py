#
# @lc app=leetcode id=3362 lang=python3
#
# [3362] Zero Array Transformation III
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
貪心
若需要選擇額外的 k 個 queries，則選擇能覆蓋更多未考慮位置的 query
"""
# @lc code=start
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        diff = [0] * (n + 1)

        queries.sort(key=lambda x: x[0])  # 按照左端點排序
        hp = []  # Max Heap 保存右端點
        s = k = 0
        for i, x in enumerate(nums):
            s += diff[i]  # 累加差分
            while k < m and queries[k][0] <= i:
                l, r = queries[k]
                heappush(hp, -r)  # 將所有左端點在 i 之前的 queries 加入堆中
                k += 1
            while s < x and hp:
                r = -heappop(hp)  # 選擇能覆蓋更多未考慮位置的 query
                if r >= i:
                    s += 1
                    diff[r + 1] -= 1
            if s < x:
                return -1
        return len(hp)  # 最後 hp 的大小即為最多可以刪除的 queries 數量
# @lc code=end

