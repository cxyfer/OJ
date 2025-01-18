#
# @lc app=leetcode.cn id=2937 lang=python3
#
# [2937] 使三个字符串相等
#

# @lc code=start
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        x, y, z = len(s1), len(s2), len(s3)
        n = min(x, y, z)
        # 枚舉剩下的字串
        ans = 0
        for i in range(n):
            if s1[i] != s2[i] or s2[i] != s3[i]:
                break
            ans += 1
        return -1 if ans == 0 else  x+y+z-3*ans

# @lc code=end
sol = Solution()
print(sol.findMinimumOperations("abc", "abb", "ab")) # 2
print(sol.findMinimumOperations("dac", "bac", "cac")) # -1
