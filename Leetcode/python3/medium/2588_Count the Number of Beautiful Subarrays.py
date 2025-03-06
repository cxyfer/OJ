#
# @lc app=leetcode.cn id=2588 lang=python3
# @lcpr version=30204
#
# [2588] 统计美丽子数组数目
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ans = s = 0
        mp = defaultdict(int)
        mp[0] = 1
        for x in nums:
            s ^= x
            ans += mp[s]
            mp[s] += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [4,3,1,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,10,4]\n
# @lcpr case=end

#

