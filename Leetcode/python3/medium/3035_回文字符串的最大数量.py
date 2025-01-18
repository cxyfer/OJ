#
# @lc app=leetcode.cn id=3035 lang=python3
#
# [3035] 回文字符串的最大数量
#
from preImport import *
# @lc code=start
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        cnt_ch = Counter() # 統計每個字母出現的次數
        cnt_len = Counter() # 統計每個字串長度出現的次數
        for word in words:
            cnt_len[len(word)] += 1
            cnt_ch += Counter(word)
        s = 0 # 能兩兩成對的字母對數
        for v in cnt_ch.values():
            s += v // 2

        ans = 0
        for k, v in sorted(cnt_len.items()):
            for _ in range(v):
                s -= k // 2 # 減去需兩兩成對的字母對數
                if s < 0: # 若字母對數不夠，則無法構建回文字串
                    return ans
                ans += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.maxPalindromesAfterOperations(["abbb","ba","aa"])) # 3
print(sol.maxPalindromesAfterOperations(["abc","ab"])) # 2
print(sol.maxPalindromesAfterOperations(["cd","ef","a"])) # 1

