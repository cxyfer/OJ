#
# @lc app=leetcode id=947 lang=python3
# @lcpr version=30204
#
# [947] Most Stones Removed with Same Row or Column
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class DSU: # Disjoint Set Union
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小
        self.cnt = n # 連通分量數量

    def find(self, x: int) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            px, py = py, px
        self.pa[py] = px
        self.sz[px] += self.sz[py]
        self.cnt -= 1
        return True

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = DSU(n)
        for i, (x, y) in enumerate(stones):
            for j in range(i + 1, n):
                if stones[j][0] == x or stones[j][1] == y:
                    dsu.union(i, j)
        return n - dsu.cnt # 要刪除的石頭數量
# @lc code=end



#
# @lcpr case=start
# [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[0,2],[1,1],[2,0],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0]]\n
# @lcpr case=end

#

