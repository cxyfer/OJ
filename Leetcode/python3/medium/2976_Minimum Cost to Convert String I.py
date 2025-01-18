#
# @lc app=leetcode id=2976 lang=python3
# @lcpr version=30204
#
# [2976] Minimum Cost to Convert String I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g = [[float("inf")] * 26 for _ in range(26)]
        for i in range(26):
            g[i][i] = 0
        for u, v, w in zip(original, changed, cost): # 初始化
            u, v = ord(u)-ord('a'), ord(v)-ord('a')
            g[u][v] = min(g[u][v], w) # 這裡要注意，因為可能有重複的邊，所以要取最小值

        # Floyd-Warshall
        for k in range(26): # 枚舉中間點
            for i in range(26): # 枚舉起點
                if g[i][k] == float("inf"): continue # 不可能由 g[i][k] 轉移到其他點
                for j in range(26): # 枚舉終點
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]) # 更新 g[i][j]
        
        ans = 0
        for u, v in zip(source, target): # 枚舉每個字元
            u, v = ord(u)-ord('a'), ord(v)-ord('a')
            if g[u][v] == float("inf"): # 不連通，不可能修改成 target
                return -1
            ans += g[u][v] # 將 u 修改成 v 的成本加總
        return ans
# @lc code=end

#
# @lcpr case=start
# "abcd"\n"acbe"\n["a","b","c","c","e","d"]\n["b","c","b","e","b","e"]\n[2,5,5,1,2,20]\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"bbbb"\n["a","c"]\n["c","b"]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"abce"\n["a"]\n["e"]\n[10000]\n
# @lcpr case=end

#

