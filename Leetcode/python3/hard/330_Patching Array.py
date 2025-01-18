#
# @lc app=leetcode id=330 lang=python3
# @lcpr version=30203
#
# [330] Patching Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """ 歸納法
        由小到大構造
        令 s 表示當前可以構造的最大值，即當前可以構造 [0, s] 中的所有整數，則 s+1 為下一個要構造的值

        若已經確定可以構造出 [0, s] 中的所有整數，此時使用 x 可以構造出 [x, s+x] 中的所有整數。
        若兩個區間有交集，即 x <= s+1 ，則可以構造出 [0, s+x] 中的所有整數。
        否則，無法構造出 s+1 ，需要補充 s+1 。

        Similar to 1798. Maximum Number of Consecutive Values You Can Make
        Same to 2952. Minimum Number of Coins to be Added
    """
    def minPatches(self, nums: List[int], n: int) -> int:
        m = len(nums)
        ans, idx, s = 0, 0, 0
        
        while s < n:
            if idx < m and nums[idx] <= s + 1:
                s += nums[idx] # 可以構造出 [0, s + nums[idx]] 中的所有整數
                idx += 1
                continue
            else: # 因為後面的數字都 > s+1 ，所以無法構造出 s+1 了，需要補充 s+1
                s += s + 1
                ans += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.minPatches([1,3],6)) # 1
print(sol.minPatches([1,5,10],20)) # 2
print(sol.minPatches([1,2,2],5)) # 0

#
# @lcpr case=start
# [1,3]\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,5,10]\n20\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n5\n
# @lcpr case=end

#

