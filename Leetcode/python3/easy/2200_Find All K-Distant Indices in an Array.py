#
# @lc app=leetcode id=2200 lang=python3
#
# [2200] Find All K-Distant Indices in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        pos = deque(i for i, x in enumerate(nums) if x == key)
        ans = []
        for i, x in enumerate(nums):
            while pos and i > pos[0] + k:
                pos.popleft()
            if not pos:
                break
            if i >= pos[0] - k:
                ans.append(i)
        return ans
# @lc code=end

