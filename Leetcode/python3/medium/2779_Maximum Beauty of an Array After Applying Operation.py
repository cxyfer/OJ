#
# @lc app=leetcode id=2779 lang=python3
# @lcpr version=30203
#
# [2779] Maximum Beauty of an Array After Applying Operation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

"""
    1. Sliding Window
    2. Prefix Sum + Difference Array
        - 在 [x-k, x+k] 區間上 +1 ， 由於比最小值更小和比最大值更大的數不會對答案有影響，因此可以轉換成在 [max(x-k, 0), min(x+k, mx)] 區間上 +1
        - 區間加法可以用差分陣列來實現，將區間 [l, r] 上的所有數 +1 可以轉換成對差分陣列的 l 位置 +1， r+1 位置 -1
        - 對差分陣列做前綴和即為每個數字的次數
"""

class Solution1:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, left = 0, 0
        for right, x in enumerate(nums): # 枚舉右端點
            while x - nums[left] > k * 2: # 保證窗口內最大值和最小值之差不超過2k
                left += 1
            ans = max(ans, right - left + 1) # 更新答案
        return ans

class Solution2:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        diff = [0] * (mx + 2)
        for x in nums:  # 在 [x-k, x+k] 區間上 +1
            diff[max(x - k, 0)] += 1
            diff[min(x + k + 1, mx + 1)] -= 1
        s = [0] * (mx + 3)  # 對 diff 做前綴和，可優化成常數空間
        for i in range(1, mx + 3):
            s[i] = s[i - 1] + diff[i - 1]
        return max(s)

class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()

print(sol.maximumBeauty([4,6,1,2], 2)) # 3
# print(sol.maximumBeauty([1,1,1,1], 10)) # 4
# print(sol.maximumBeauty([12,71], 10)) # 1
# print(sol.maximumBeauty([48,93,96,19], 24)) # 3

#
# @lcpr case=start
# [4,6,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n10\n
# @lcpr case=end

#
