#
# @lc app=leetcode.cn id=1887 lang=python3
#
# [1887] 使数组元素相等的减少操作次数
#
from preImport import *
# @lc code=start
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        # 統計比自己小的數字有幾種
        keys = sorted(cnt.keys())
        pre = []
        for key in keys:
            pre.append((pre[-1]+1 if pre else 0))
        ans = 0
        for i, k in enumerate(keys):
            ans += cnt[k] * pre[i]
        return ans
# @lc code=end

# @test([5,1,3])=3
# @test([1,1,1])=0
# @test([1,1,2,2,3])=4

sol = Solution()
print(sol.reductionOperations([5,1,3])) # 3
print(sol.reductionOperations([1,1,1])) # 0
print(sol.reductionOperations([1,1,2,2,3])) # 4