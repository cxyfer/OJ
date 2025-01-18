#
# @lc app=leetcode id=2766 lang=python3
# @lcpr version=30204
#
# [2766] Relocate Marbles
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        st = set(nums)
        for f, t in zip(moveFrom, moveTo):
            st.remove(f)
            st.add(t)
        return sorted(st)
# @lc code=end

sol = Solution()
print(sol.relocateMarbles([3,4], [4,3,1,2,2,3,2,4,1], [3,1,2,2,3,2,4,1,1]))

#
# @lcpr case=start
# [1,6,7,8]\n[1,7,2]\n[2,9,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,3,3]\n[1,3]\n[2,2]\n
# @lcpr case=end

#

