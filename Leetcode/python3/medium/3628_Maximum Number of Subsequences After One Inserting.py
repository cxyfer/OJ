#
# @lc app=leetcode id=3628 lang=python3
#
# [3628] Maximum Number of Subsequences After One Inserting
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. LCS DP + 前後綴分解

考慮插入每種字元後增加的 LCT 子序列個數：
1. 插入 L：貢獻為插入位置右側的 CT 數量，將 L 插入到最左邊，所得貢獻最大
2. 插入 C：貢獻為插入位置左側的 L 數量乘上右側的 T 數量，可以前後綴分解計算
3. 插入 T：貢獻為插入位置左側的 LC 數量，將 T 插入到最右邊，所得貢獻最大

使用 115. Distinct Subsequences 的解法計算 s 中 LCT/LC/CT 的子序列數量即可

2. 狀態機 DP
由於目標字串只有 3 種字元，可以輕易的計算以單前字元為結尾的子序列數量：
1. 當前字元為 L 時，l 的子序列數量增加 1
2. 當前字元為 C 時，c 的子序列數量增加 1、lc 的子序列數量增加 l
3. 當前字元為 T 時，lct 的子序列數量增加 lc、ct 的子序列數量增加 c
如此便能求出前述方法中的 LCT/LC/CT 子序列數量，可以結合前後綴分解 LT 的貢獻
"""
# @lc code=start
class Solution1:
    def numOfSubsequences(self, s: str) -> int:
        lt = 0
        l, t = 0, s.count('T')
        for i, c in enumerate(s):
            if c == 'L':
                l += 1
            elif c == 'T':
                t -= 1
            lt = max(lt, l * t)
        return self.numDistinct(s, "LCT") + max(lt, self.numDistinct(s, "LC"), self.numDistinct(s, "CT"))

    # 115. Distinct Subsequences
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        f = [1] + [0] * m
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                if s[i - 1] == t[j - 1]:
                    f[j] += f[j - 1]
        return f[m]

class Solution2:
    def numOfSubsequences(self, s: str) -> int:
        t = s.count('T')
        l = lc = lct = c = ct = 0
        lt = 0
        for ch in s:
            if ch == 'L':
                l += 1
            elif ch == 'C':
                c += 1
                lc += l
            elif ch == 'T':
                ct += c
                lct += lc
                t -= 1
            lt = max(lt, l * t)
        return lct + max(lt, lc, ct)

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.numOfSubsequences("LMCT"))  # 2
print(sol.numOfSubsequences("LCCT"))  # 4
print(sol.numOfSubsequences("L"))  # 0
