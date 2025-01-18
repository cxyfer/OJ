#
# @lc app=leetcode id=2593 lang=python3
# @lcpr version=30204
#
# [2593] Find Score of an Array After Marking All Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        hp = [(x, i) for i, x in enumerate(nums)]
        heapify(hp)
        ans = 0
        used = [False] * n
        while hp:
            x, idx = heappop(hp)
            if used[idx]:
                continue
            ans += x
            used[idx] = True
            if idx - 1 >= 0:
                used[idx - 1] = True
            if idx + 1 < n:
                used[idx + 1] = True
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,1,3,4,5,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,1,3,2]\n
# @lcpr case=end

#

