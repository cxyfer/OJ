#
# @lc app=leetcode id=2070 lang=python3
# @lcpr version=30204
#
# [2070] Most Beautiful Item for Each Query
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort(key=lambda x: x[0])
        for i in range(1, n):
            items[i][1] = max(items[i][1], items[i - 1][1])
        ans = []
        for q in queries:
            idx = bisect_right(items, [q, float('inf')]) - 1
            ans.append(items[idx][1] if idx >= 0 else 0)
        return ans
# @lc code=end

sol = Solution()
print(sol.maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6])) # [2,4,5,5,6,6]
print(sol.maximumBeauty([[1,2],[1,2],[1,3],[1,4]], [1])) # [3]
print(sol.maximumBeauty([[10,1000]], [5])) # [1]
# @lcpr case=start
# [[1,2],[3,2],[2,4],[5,6],[3,5]]\n[1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,2],[1,3],[1,4]]\n[1]\n
# @lcpr case=end

# @lcpr case=start
# [[10,1000]]\n[5]\n
# @lcpr case=end

#

