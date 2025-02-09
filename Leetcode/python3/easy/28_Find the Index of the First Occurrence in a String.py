#
# @lc app=leetcode id=28 lang=python3
# @lcpr version=30204
#
# [28] Find the Index of the First Occurrence in a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def strStr(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        pi = [0] * m
        ln = 0
        for i in range(1, m):
            while ln and t[i] != t[ln]:
                ln = pi[ln - 1]
            if t[i] == t[ln]:
                ln += 1
            pi[i] = ln
        ln = 0
        for i in range(n):
            while ln and s[i] != t[ln]:
                ln = pi[ln - 1]
            if s[i] == t[ln]:
                ln += 1
            if ln == m:
                return i - m + 1
        return -1

from random import randint

MOD = 1070777777
BASE = randint(int(1e8), int(1e9))

class Solution2:
    def strStr(self, text: str, t: str) -> int:
        n, m = len(text), len(t)
        if n < m:
            return -1

        # Rabin-Karp Rolling Hash
        P = [1] * (m + 1)  # P[i] = BASE^i % MOD
        H = [0] * (m + 1)  # H[i] = hash(s[:i])
        for i in range(m):
            P[i + 1] = (P[i] * BASE) % MOD
            H[i + 1] = (H[i] * BASE + ord(t[i])) % MOD
 
        # Sliding window
        hs = 0
        for i, ch in enumerate(text):
            hs = (hs * BASE + ord(ch)) % MOD  # 入窗口
            if i >= m:  # 出窗口，維持窗口大小為 m
                hs = (hs - ord(text[i - m]) * P[m]) % MOD
            # 比較雜湊值和字串，若不考慮碰撞則比較雜湊值即可
            if i >= m - 1 and hs == H[m] and text[i - m + 1:i + 1] == t:
                return i - m + 1
        return -1

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.strStr("sadbutsad", "sad"))
print(sol.strStr("aaa", "aaaa"))
#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end


# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#

