# You are given an integer n.
#  A string s is called good if it contains only lowercase English characters and it is possible to rearrange the characters of s such that the new string contains "leet" as a substring.
#  For example:  The string "lteer" is good because we can rearrange it to form "leetr" .
# "letl" is not good because we cannot rearrange it to contain "leet" as a substring.
# Return the total number of good strings of length n.
#  Since the answer may be large, return it modulo 109 + 7.
#  A substring is a contiguous sequence of characters within a string.


class Solution:
    def stringCount(self, n: int) -> int:
        # return self.solveByPIE(n)
        return self.solveByDP(n)
    """
        1. 排容原理
        l, e, t 的數量不小於 1, 2, 1
    """
    def solveByPIE(self, n: int) -> int:
        MOD = 10**9 + 7
        res0 = pow(26, n, MOD)
        # res1 = (pow(25, n, MOD) + (pow(25, n, MOD) + pow(25, n-1, MOD) * n) + pow(25, n, MOD)) % MOD
        res1 = (75 + n) * pow(25, n - 1, MOD)
        # res2 = 2 * (pow(24, n, MOD) + n * pow(24, n - 1, MOD))  + pow(24, n, MOD)
        res2 = (72 + 2 * n) * pow(24, n - 1, MOD)
        # res3 = pow(23, n, MOD) + n * pow(23, n - 1, MOD)
        res3 =  ((23 + n) * pow(23, n - 1, MOD)) % MOD
        return (res0 - res1 + res2 - res3) % MOD
    """
        2. Dynamic Programming
        dp[n][i][j][k] 為長度為 n, 且 l, e, t 的數量分別為 i, j, k 的字串數量
        l, e, t 的數量不小於 1, 2, 1
    """
    def solveByDP(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[[0 for k in range(2)] for j in range(3)] for i in range(2)] for _ in range(n+1)]
        dp[0][0][0][0] = 1
        for i in range(1, n+1):
            for l in range(2):
                for e in range(3):
                    for t in range(2):
                        dp[i][l][e][t] = dp[i-1][l][e][t] * 23 % MOD # 第i個字元非 l, e, t
                        if l > 0: # 第i個字元為 l
                            dp[i][l][e][t] += (dp[i-1][l-1][e][t] + dp[i-1][l][e][t]) % MOD
                            dp[i][l][e][t] %= MOD
                        if t > 0:
                            dp[i][l][e][t] += (dp[i-1][l][e][t-1] + dp[i-1][l][e][t]) % MOD
                            dp[i][l][e][t] %= MOD
                        if e > 0:
                            dp[i][l][e][t] += dp[i-1][l][e-1][t]
                            dp[i][l][e][t] %= MOD
                            if e == 2:
                                dp[i][l][e][t] += dp[i-1][l][e][t]
                                dp[i][l][e][t] %= MOD
        return dp[n][1][2][1] % MOD

sol = Solution()
print(sol.stringCount(4)) # 12
print(sol.stringCount(5)) # 1460
print(sol.stringCount(10)) 
        
# cnt = 0
# print(ascii_lowercase)
# for a in ascii_lowercase:
#     for b in ascii_lowercase:
#         for c in ascii_lowercase:
#             for d in ascii_lowercase:
#                 for e in ascii_lowercase:
#                     s = a + b + c + d + e
#                     if s.count('l') >= 1 and s.count('e') >= 2 and s.count('t') >= 1:
#                         print(s)
#                         cnt += 1
# print(cnt) # 1460

# ans = 0
# for a in ascii_lowercase:
#     s = a + 'leet'
#     cnt = Counter(s)
#     tmp = factorial(5)
#     for k, v in cnt.items():
#         tmp //= factorial(v)
#     ans += tmp
# print(ans) # 1460