#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def rotateString(self, s: str, t: str) -> bool:
        return len(s) == len(t) and t in (s + s)

class Solution2a:
    def rotateString(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        pi = [0] * m
        ln = 0
        for i in range(1, m):
            while ln and t[i] != t[ln]:
                ln = pi[ln - 1]
            if t[i] == t[ln]:
                ln += 1
            pi[i] = ln
        ln = 0
        for i in range(n << 1):
            ch = s[i % n]
            while ln and ch != t[ln]:
                ln = pi[ln - 1]
            if ch == t[ln]:
                ln += 1
            if ln == m:
                return True
        return False

class Solution2b:
    def rotateString(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        s = t + "#" + s + s
        n = len(s)
        pi = [0] * n
        ln = 0
        for i in range(1, n):
            while ln and s[i] != s[ln]:
                ln = pi[ln - 1]
            if s[i] == s[ln]:
                ln += 1
            if ln == m:
                return True
            pi[i] = ln
        return False

MOD = 1070777777
BASE = randint(int(1e8), int(1e9))

class Solution3:
    def rotateString(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        s = s + s

        # Rolling Hash
        P = [1] * (m + 1)  # P[i] = BASE^i % MOD
        H = [0] * (m + 1)  # H[i] = hash(t[:i])
        for i in range(m):
            P[i + 1] = (P[i] * BASE) % MOD
            H[i + 1] = (H[i] * BASE + ord(t[i])) % MOD
 
        # Sliding window
        hs = 0
        for i in range(n << 1):
            ch = s[i % n]
            hs = (hs * BASE + ord(ch)) % MOD  # 入窗口
            if i >= m:  # 出窗口，維持窗口大小為 m
                hs = (hs - ord(s[(i - m) % n]) * P[m]) % MOD
            # 比較雜湊值和子字串，若不考慮碰撞則比較雜湊值即可
            if i >= m - 1 and hs == H[m]:
                return True
        return False

# Solution = Solution1
Solution = Solution2a
# Solution = Solution2b
# Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.rotateString("aa", "a")) # False