#
# @lc app=leetcode id=765 lang=python3
# @lcpr version=30204
#
# [765] Couples Holding Hands
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.sz = [1] * n
        self.cnt = n

    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy: return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.fa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True
    
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        uf = UnionFind(n)

        # 把相鄰位置的人 union 起來，若兩人不是同一對，則最終會形成 cycle
        for i in range(0, n, 2):
            uf.union(row[i] // 2, row[i + 1] // 2)

        # n // 2 對情侶中，需要交換的情侶數量為每個 cycle 的長度 - 1
        ans = 0
        for i in range(n // 2):
            if uf.find(i) != i:
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,0,1]\n
# @lcpr case=end

#

