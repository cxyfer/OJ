#
# @lc app=leetcode id=2799 lang=python3
# @lcpr version=30204
#
# [2799] Count Complete Subarrays in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        need = len(set(nums))
        ans = left = have = 0
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            cnt[x] += 1
            if cnt[x] == 1:
                have += 1
            while have == need:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    have -= 1
                left += 1
            ans += left
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,3,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5]\n
# @lcpr case=end

#

