#
# @lc app=leetcode id=1438 lang=python3
# @lcpr version=30204
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList

class Solution1:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        sl = SortedList()
        ans = left = 0
        for right in range(n):
            sl.add(nums[right])
            while sl[-1] - sl[0] > limit:
                sl.remove(nums[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    
class Solution2:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        q_min, q_max = deque(), deque() # 分別維護最小值和最大值的下標
        ans = left = 0
        for right in range(n):
            while q_min and nums[right] < q_min[-1]: # 維護 q_min 的單調遞增性
                q_min.pop()
            while q_max and nums[right] > q_max[-1]: # 維護 q_max 的單調遞減性
                q_max.pop()
            q_min.append(nums[right])
            q_max.append(nums[right])
            while q_max[0] - q_min[0] > limit: # 當最大值和最小值的差值大於 limit 時，移動 left
                if nums[left] == q_min[0]:
                    q_min.popleft()
                if nums[left] == q_max[0]:
                    q_max.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.longestSubarray([8,2,4,7], 4)) # 2
print(sol.longestSubarray([10,1,2,4,7,2], 5)) # 4
print(sol.longestSubarray([4,2,2,2,4,4,2,2], 0)) # 3

#
# @lcpr case=start
# [8,2,4,7]\n4\n
# @lcpr case=end

# @lcpr case=start
# [10,1,2,4,7,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,2,2,2,4,4,2,2]\n0\n
# @lcpr case=end

#

