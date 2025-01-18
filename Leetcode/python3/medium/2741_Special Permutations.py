#
# @lc app=leetcode id=2741 lang=python3
# @lcpr version=30204
#
# [2741] Special Permutations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

"""
    狀態壓縮 DP ：排列型相鄰相關
    0 為未選擇，1 為已選擇

    Similar to 526. Beautiful Arrangement
"""
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        u = (1 << n) - 1 # 全部選擇

        @cache
        def dfs(s: int, i: int) -> int: # s: 已選擇的集合, i: 前一個選擇的 index
            if s == u:
                return 1
            res = 0
            pre = nums[i]
            for j, x in enumerate(nums): # 枚舉下一個選擇的 index
                if (s >> j) & 1: # 已選擇過
                    continue
                if pre % x == 0 or x % pre == 0: # 符合條件
                    res += dfs(s | (1 << j), j)
            return res
        
        return sum(dfs(1 << i, i) % MOD for i in range(n)) % MOD
# @lc code=end


sol = Solution()
print(sol.specialPerm([2,3,6])) # 2
print(sol.specialPerm([1,4,3])) # 2
print(sol.specialPerm([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192])) # 178290591

#
# @lcpr case=start
# [2,3,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,3]\n
# @lcpr case=end

#

