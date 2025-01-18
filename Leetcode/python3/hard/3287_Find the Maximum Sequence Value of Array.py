#
# @lc app=leetcode id=3287 lang=python3
# @lcpr version=30204
#
# [3287] Find the Maximum Sequence Value of Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # 令 dp1[i][j] 表示在前 i 個元素中選 j 個的 OR 值集合
        dp1 = [ [set() for _ in range(k+1)] for _ in range(n+1) ]
        dp1[0][0].add(0)
        
        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(0, k+1):
                # 不選擇第 i 個元素，繼承前一個狀態
                dp1[i][j].update(dp1[i-1][j])
                # 選擇第 i 個元素
                if j == 0:
                    continue
                for or_val in dp1[i-1][j-1]:
                    dp1[i][j].add(or_val | num)
        
        # 令 dp2[i][j] 表示在第 i 個元素到最後一個元素中選 j 個的 OR 值集合
        dp2 = [ [set() for _ in range(k+1)] for _ in range(n+1) ]
        dp2[n][0].add(0)
        
        for i in range(n-1, -1, -1):
            num = nums[i]
            for j in range(0, k+1):
                # 不選擇第 i 個元素，繼承後一個狀態
                dp2[i][j].update(dp2[i+1][j])
                # 選擇第 i 個元素
                if j == 0:
                    continue
                for or_val in dp2[i+1][j-1]:
                    dp2[i][j].add(or_val | num)
        
        ans = 0
        # 枚舉所有可能的分割點
        for i in range(k, n - k + 1):
            for or1 in dp1[i][k]:
                for or2 in dp2[i][k]:
                    ans = max(ans, or1 ^ or2)
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,6,7]\n1\n
# @lcpr case=end

# @lcpr case=start
# [4,2,5,6,7]\n2\n
# @lcpr case=end

#

