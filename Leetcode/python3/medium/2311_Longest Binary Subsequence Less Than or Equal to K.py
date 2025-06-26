#
# @lc app=leetcode id=2311 lang=python3
#
# [2311] Longest Binary Subsequence Less Than or Equal to K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
兩種思路：
1. 考慮貪心地保留，從低位開始保留可以保留最多 1 (Solution1)
  - 若某位開始無法保留，則前面的更不能保留，可以提前結束 (Solution2)
2. 考慮貪心地刪除，從高位開始刪除可以刪除最少 1 (Solution3a)
  - 但這樣需要事先計算若全部保留的值，這在其他語言會 overflow，但由於 k 的限制，可以只計算前 30 位 (Solution3b)
"""
# @lc code=start
class Solution1:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0
        for i, b in enumerate(reversed(s)):
            if b == '1':
                if (v := 1 << i) > k:  # 這個 1 不能保留
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
                    ans -= s[:-i].count('1')  # 前面的所有 1 都不能保留了
                    break
                k -= v
        return ans

class Solution3a:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = ans = len(s)
        v = 0
        for i, b in enumerate(s):
            v |= int(b == '1') << (n - i - 1)
        for i, b in enumerate(s):
            if b == '1':
                if v <= k:
                    break
                v ^= 1 << (n - i - 1)
                ans -= 1
        return ans

class Solution3b:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        ans = n
        v = 0
        for i in range(max(n - 30, 0), n):
            v = (v << 1) + int(s[i] == '1')
        for i, b in enumerate(s):
            if b == '1':
                if (n - i - 1) >= 30:
                    ans -= 1
                    continue
                if v <= k:
                    break
                v ^= 1 << (n - i - 1)
                ans -= 1
        return ans

# Solution = Solution1 
# Solution = Solution2
# Solution = Solution3a
Solution = Solution3b
# @lc code=end

sol = Solution()
print(sol.longestSubsequence(s = "1001010", k = 5))  # 5
print(sol.longestSubsequence(s = "00101001", k = 1))  # 6
print(sol.longestSubsequence(s = "11111", k = int("10000", 2)))  # 4

print(sol.longestSubsequence(s = "001010101011010100010101101010010", k = 93951055))  # 31
