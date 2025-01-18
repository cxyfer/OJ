#
# @lc app=leetcode.cn id=1759 lang=python3
#
# [1759] 统计同质子字符串的数目
#

# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        ans = l = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                l += 1
            else:
                l = 1
            ans += l % MOD
        return ans % MOD
# @lc code=end
sol = Solution()
print(sol.countHomogenous("abbcccaa")) # 13
print(sol.countHomogenous("xy")) # 2
print(sol.countHomogenous("zzzzz")) # 15

