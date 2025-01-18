#
# @lc app=leetcode id=1509 lang=python3
# @lcpr version=30204
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. 直接排序
     - 從不變部分的角度思考，改變 3 個數字後，會有 n - 3 個數字不變
       因此考慮不變部分的最大值和最小值差距即可
     - 從貪心的角度思考，改變的數字應該從最大和最小的 3 個數字中選擇
       因此可以改變最小的 k 個數字和最大的 3 - k 個數字，其中 0 <= k <= 3
       總共有 4 種情況，分別計算出來後取最小值即可
     - 以上兩種方式雖然思路不同，但操作是一樣的

        若改變三個數字後，則最多會有 n - 3 個數字不變
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        k = n - 3 # 窗口大小
        ans = nums[-1] - nums[0]
        for i in range(n - k + 1):
            j = i + k - 1
            ans = min(ans, nums[j] - nums[i])
        return ans
# @lc code=end

sol = Solution()
print(sol.minDifference([1,5,0,10,14])) # 1
print(sol.minDifference([6,6,0,1,1,4,6])) # 2

#
# @lcpr case=start
# [5,3,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,5,0,10,14]\n
# @lcpr case=end

# @lcpr case=start
# [3,100,20]\n
# @lcpr case=end

#

