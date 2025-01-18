#
# @lc app=leetcode id=2501 lang=python3
# @lcpr version=30204
#
# [2501] Longest Square Streak in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def longestSquareStreak(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        for x in nums:
            cnt = 0
            while x in st:
                cnt += 1
                x *= x
            ans = max(ans, cnt)
        return ans if ans >= 2 else -1

class Solution2:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        f = defaultdict(int)
        ans = 1
        for x in nums:
            if x * x in f:
                f[x] = f[x * x] + 1
                ans = max(ans, f[x])
            else:
                f[x] = 1
        return ans if ans >= 2 else -1
    
class Solution3:
    def longestSquareStreak(self, nums: List[int]) -> int:
        st = set(nums)
        @cache
        def dfs(x: int) -> int:
            if x not in st: return 0
            return 1 + dfs(x * x)
        ans = 0
        for x in st:
            ans = max(ans, dfs(x))
        return ans if ans >= 2 else -1
    
# class Solution(Solution1):
class Solution(Solution2):
# class Solution(Solution3):
    pass
# @lc code=end



#
# @lcpr case=start
# [4,3,6,16,8,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,6,7]\n
# @lcpr case=end

#

