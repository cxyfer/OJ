#
# @lc app=leetcode id=3162 lang=python3
# @lcpr version=30202
#
# [3162] Find the Number of Good Pairs I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for x in nums1:
            if x % k != 0: continue
            for y in nums2:
                if x % (y * k) == 0:
                    ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,3,4]\n[1,3,4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,12]\n[2,4]\n3\n
# @lcpr case=end

#

