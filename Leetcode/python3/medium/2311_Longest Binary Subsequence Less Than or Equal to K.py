#
# @lc app=leetcode id=2311 lang=python3
#
# [2311] Longest Binary Subsequence Less Than or Equal to K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0
        for i, b in enumerate(reversed(s)):
            if b == '1':
                if (v := 1 << i) > k:
                    continue
                k -= v
            ans += 1
        return ans
    
class Solution2:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = len(s)
        for i, b in enumerate(reversed(s)):
            if b == '1':
                if (v := 1 << i) > k:
                    ans -= s[:-i].count('1')
                    break
                k -= v
        return ans

# Solution = Solution1 
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.longestSubsequence(s = "1001010", k = 5))  # 5
print(sol.longestSubsequence(s = "00101001", k = 1))  # 6
print(sol.longestSubsequence(s = "11111", k = int("10000", 2)))  # 4

print( int("10000", 2))