#
# @lc app=leetcode id=1316 lang=python3
# @lcpr version=30204
#
# [1316] Distinct Echo Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = 1070777777
BASE = randint(int(1e8), int(1e9))
class HashString:
    # 初始化 HashString ，預計算所有冪次和前綴雜湊
    def __init__(self, s: str):
        self.n = len(s)
        self.P = [1] + [0] * self.n  # P[i] = BASE^i % MOD
        self.H = [0] * (self.n + 1)  # H[i] = hash(s[:i])
        
        for i, b in enumerate(s):
            # 預計算所有冪次
            self.P[i + 1] = self.P[i] * BASE % MOD
            # 預計算所有前綴雜湊
            self.H[i + 1] = (self.H[i] * BASE + ord(b)) % MOD 

    # 計算子字串 s[l..r] 的雜湊值 (0-indexed)，計算方法類似前綴和
    def query(self, l: int, r: int) -> int:
        return (self.H[r + 1] - self.H[l] * self.P[r - l + 1]) % MOD
    
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        hs = HashString(text)
        st = set()
        for i in range(n):
            for m in range(1, (n-i) // 2 + 1):
                left = hs.query(i, i + m - 1)
                right = hs.query(i + m, i + 2 * m - 1)
                if left == right:
                    st.add(left)
        return len(st)
# @lc code=end

sol = Solution()
print(sol.distinctEchoSubstrings("abcabcabc"))  # 3
print(sol.distinctEchoSubstrings("leetcodeleetcode"))  # 2

#
# @lcpr case=start
# "abcabcabc"\n
# @lcpr case=end

# @lcpr case=start
# "leetcodeleetcode"\n
# @lcpr case=end

#

