#
# @lc app=leetcode id=3097 lang=python3
# @lcpr version=30204
#
# [3097] Shortest Subarray With OR at Least K II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        mp = dict()
        for i, x in enumerate(nums):
            mp = {or_ | x: left for or_, left in mp.items()}
            mp[x] = i  # 只包含 x 的子数组
            for or_, left in mp.items():
                if or_ >= k:
                    ans = min(ans, i - left + 1)
        return ans if ans < float('inf') else -1
    
class Solution2:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        cnt = [0] * 32
        left = cur = 0
        for right, x in enumerate(nums):
            # 1. 入窗口
            for b in range(32):
                if x & (1 << b):
                    cnt[b] += 1
                    if cnt[b] == 1:
                        cur |= 1 << b
   
            while left <= right and cur >= k:
                # 2. 更新答案
                ans = min(ans, right - left + 1)
                # 3. 出窗口
                y = nums[left]
                for b in range(32):
                    if y & (1 << b):
                        cnt[b] -= 1
                        if cnt[b] == 0:
                            cur ^= 1 << b
                left += 1

        return ans if ans < float('inf') else -1

class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.minimumSubarrayLength([1,2,3], 2))  # 1
print(sol.minimumSubarrayLength([2,1,8], 10))  # 3
print(sol.minimumSubarrayLength([1,2], 0))  # 1
print(sol.minimumSubarrayLength([1,2,3], 100))  # -1
#
# @lcpr case=start
# [1,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,1,8]\n10\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

#

