#
# @lc app=leetcode.cn id=2609 lang=python3
#
# [2609] 最长平衡子字符串
#

# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        cnt0, cnt1 = 0, 0 # 0之後的連續0數量、連續1數量
        for ch in s:
            if ch == '0':
                if cnt1 > 0:
                    cnt0, cnt1 = 0, 0
                cnt0 += 1
            else:
                cnt1 += 1
            ans = max(ans, min(cnt0, cnt1) * 2)
        return ans
# @lc code=end
sol = Solution()
print(sol.findTheLongestBalancedSubstring("01000111")) # 6
print(sol.findTheLongestBalancedSubstring("00111")) # 4
print(sol.findTheLongestBalancedSubstring("111")) # 0

