#
# @lc app=leetcode id=2573 lang=python3
#
# [2573] Find the String with LCP
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n))  # 父節點
        self.sz = [1] * n  # 連通分量大小
        self.cnt = n  # 連通分量數量

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True

class Solution1:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        for i, row in enumerate(lcp):
            if row[i] != n - i:
                return ''
            for j in range(i + 1, n):
                if row[j] != lcp[j][i] or row[j] > n - j:
                    return ''

        uf = UnionFind(n)
        for i, row in enumerate(lcp):
            for j in range(i + 1, n):
                if row[j] > 0:
                    uf.union(i, j)

        mp = [-1] * n
        comps = []
        for u in range(n):
            fu = uf.find(u)
            if mp[fu] == -1:
                mp[fu] = len(comps)
                comps.append([])
            comps[mp[fu]].append(u)

        if len(comps) > 26:
            return ''
        
        ans = [''] * n
        for i, comp in enumerate(comps):
            for u in comp:
                ans[u] = chr(ord('a') + i)
        
        # 這裡的寫法是假設 lcp 已經是對稱的情況
        lcp2 = [[0] * (n + 1) for _ in range(n + 1)]
        for ln in range(1, n + 1):
            for i in range(n - ln, -1, -1):
                j = i + ln - 1
                if ans[i] == ans[j]:
                    lcp2[i][j] = lcp2[i + 1][j + 1] + 1
                else:
                    lcp2[i][j] = 0
                if lcp2[i][j] != lcp[i][j]:
                    return ''
        return ''.join(ans)

class Solution2:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # 透過 lcp 矩陣可以找到必須為相同字元的索引，採用貪心的方式由小到大填入字元
        s = [''] * n
        i = 0
        for ch in ascii_lowercase:
            s[i] = ch
            for j in range(i + 1, n):
                # 如果 lcp[i][j] > 0，代表 s[i] 和 s[j] 是相同的字元
                if lcp[i][j] > 0:
                    s[j] = ch
            # 找到下一個還沒填入字元的索引
            while i < n and s[i] != '':
                i += 1
            if i == n:
                break
            
        # 用完所有字元，但還有空位，說明無法構造出符合 LCP 矩陣的字串
        # if any(c == '' for c in s):
        if i < n:
            return ""
        
        # 驗證構造的字串是否符合 LCP 矩陣
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 計算構造的字串的 LCP
                exp = (lcp[i + 1][j + 1] if i < n - 1 and j < n - 1 else 0) + 1 if s[i] == s[j] else 0
                # 若與 LCP 矩陣不符，則說明無法構造出符合 LCP 矩陣的字串
                if lcp[i][j] != exp:
                    return ""
        return ''.join(s)

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.findTheString([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]))  # "abab"


print(sol.findTheString([[2,0],[1,1]]))  # ""