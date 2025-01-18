#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ans = 0
        # lcnt0, rcnt1 = 0, s.count('1')
        cur = s.count('1')
        for ch in s[:n-1]:
            # if ch == '0':
            #     lcnt0 += 1
            # else:
            #     rcnt1 -= 1
            cur += 1 if ch == '0' else -1
            # ans = max(ans, lcnt0 + rcnt1)
            ans = max(ans, cur)
        return ans
# @lc code=end
sol = Solution()
print(sol.maxScore("011101")) # 5
print(sol.maxScore("00111")) # 5
print(sol.maxScore("1111")) # 3
print(sol.maxScore("00")) # 1
