#
# @lc app=leetcode.cn id=2342 lang=python3
#
# [2342] 数位和相等数对的最大和
#
from preImport import *
# @lc code=start
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        for num in nums:
            sod = sum(map(int, list(str(num))))
            cnt[sod].append(num)
        ans = -1
        for key in cnt:
            if len(cnt[key]) < 2:
                continue
            cnt[key].sort(reverse=True)
            ans = max(ans, cnt[key][0] + cnt[key][1])
        return ans
# @lc code=end

# @test([18,43,36,13,7])=54
# @test([10,12,19,14])=-1

sol = Solution()
print(sol.maximumSum([18,43,36,13,7])) # 54
print(sol.maximumSum([10,12,19,14])) # -1

