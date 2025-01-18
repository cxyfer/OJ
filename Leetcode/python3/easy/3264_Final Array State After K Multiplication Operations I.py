#
# @lc app=leetcode id=3264 lang=python3
# @lcpr version=30204
#
# [3264] Final Array State After K Multiplication Operations I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hp = [(x, i) for i, x in enumerate(nums)]
        heapify(hp)
        ans = [x for x in nums]
        for _ in range(k):
            x, idx = heappop(hp)
            ans[idx] = x * multiplier
            heappush(hp, (x * multiplier, idx))
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,1,3,5,6]\n5\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n3\n4\n
# @lcpr case=end

#

