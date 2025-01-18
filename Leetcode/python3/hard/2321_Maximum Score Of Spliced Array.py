#
# @lc app=leetcode id=2321 lang=python3
# @lcpr version=30203
#
# [2321] Maximum Score Of Spliced Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        從 nums1 或 nums2 還能變大多少下去思考
        
        令 diff = nums1 - nums2 
        則 diff 的最大連續子陣列和就是 nums2 可以變大的差值，
        反過來說，diff 的最小連續子陣列和的絕對值也是 nums1 可以變大的差值
    """
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = [x - y for x, y in zip(nums1, nums2)]
        dp1 = [0] * (n + 1) # 差的最大值
        dp2 = [0] * (n + 1) # 差的最小值
        for i, x in enumerate(diff):
            dp1[i + 1] = max(dp1[i] + x, x)
            dp2[i + 1] = min(dp2[i] + x, x)
        return max(sum(nums2) + max(dp1), sum(nums1) - min(dp2))
# @lc code=end



#
# @lcpr case=start
# [60,60,60]\n[10,90,10]\n
# @lcpr case=end

# @lcpr case=start
# [20,40,20,70,30]\n[50,20,50,40,20]\n
# @lcpr case=end

# @lcpr case=start
# [7,11,13]\n[1,1,1]\n
# @lcpr case=end

#

