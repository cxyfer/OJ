#
# @lc app=leetcode id=3066 lang=python3
# @lcpr version=30204
#
# [3066] Minimum Operations to Exceed Threshold Value II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hp = [x for x in nums]
        heapify(hp)
        ans = 0
        while hp[0] < k:
            x = heappop(hp)
            # y = heappop(hp)
            # heappush(hp, x * 2 + y)
            heapreplace(hp, x * 2 + hp[0])
            ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,11,10,1,3]\n10\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,4,9]\n20\n
# @lcpr case=end

#

