#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-endpreImport import *
# @lc code=start
class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lst = defaultdict(lambda : float("-inf"))
        for i, x in enumerate(nums):
            if i - lst[x] <= k:
                return True
            lst[x] = i
        return False
    
class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            cnt[x] += 1
            if cnt[x] > 1:
                return True
            if i >= k:
                cnt[nums[i - k]] -= 1
        return False
class Solution(Solution2):
    pass
# @lc code=end

