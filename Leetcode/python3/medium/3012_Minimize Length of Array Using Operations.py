#
# @lc app=leetcode id=3012 lang=python3
#
# [3012] Minimize Length of Array Using Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
思維
如果對 x 和 y (x < y) 進行操作，由於 x % y = x，等同於保留 x 刪除 y。
因此可以令最小數 mn 當作 x，把所有 > mn 的數都刪除，最後剩下的數就是 mn。
顯然當只有一個最小數時，這種方案是最優的；但如果有多個最小數時，則不是。
故考慮能否構建出更小的數，由於任何數 % mn 都 < mn，因此若存在 x > mn 且 x % mn != 0，則可以構建出更小的數。
只有當所有數都是 mn 的倍數時，才不能構建出更小的數，此時只能對 mn 兩兩消除。
"""
# @lc code=start
class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        mn = min(nums)
        for x in nums:
            if x % mn != 0:  # 能構造出更小的數
                return 1
        return math.ceil(nums.count(mn) / 2)
# @lc code=end

