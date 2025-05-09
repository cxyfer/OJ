#
# @lc app=leetcode.cn id=100104 lang=python3
#
# [100104] 使二进制字符串变美丽的最少修改次数
#

# @lc code=start
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n//2):
            if s[2*i] != s[2*i+1]:
                ans += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.minChanges("0100")) # 1
print(sol.minChanges("10")) # 1
print(sol.minChanges("1110")) # 1
