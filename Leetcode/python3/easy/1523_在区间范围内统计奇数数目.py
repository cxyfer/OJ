#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        interval = high - low + 1
        if low & 1 and high & 1:
            return interval // 2 + 1
        else:
            return interval // 2
# @lc code=end
sol = Solution()
# @test(3,7)=3
# @test(8,10)=1
print(sol.countOdds(3,6)) # 2
print(sol.countOdds(3,7)) # 3
print(sol.countOdds(4,6)) # 1
print(sol.countOdds(4,7)) # 2
print(sol.countOdds(8,10)) # 1
print(sol.countOdds(8,11)) # 2

