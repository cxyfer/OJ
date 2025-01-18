#
# @lc app=leetcode id=2530 lang=python3
# @lcpr version=30204
#
# [2530] Maximal Score After Applying K Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hp = [-x for x in nums]
        heapify(hp)
        ans = 0
        for _ in range(k):
            x = -heappop(hp)
            ans += x
            # heappush(hp, -math.ceil(x / 3))
            heappush(hp, -((x + 2) // 3))
        return ans
# @lc code=end



#
# @lcpr case=start
# [10,10,10,10,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,10,3,3,3]\n3\n
# @lcpr case=end

#

