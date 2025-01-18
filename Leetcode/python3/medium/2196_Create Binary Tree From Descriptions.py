#
# @lc app=leetcode id=2196 lang=python3
# @lcpr version=30204
#
# [2196] Create Binary Tree From Descriptions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class DSU: # Disjoint Set Union
    __slots__ = ['n', 'pa']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點

    def find(self, x: int) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.pa[py] = px
        return True
    
class Solution1:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        N = int(1e5 + 5)
        dsu = DSU(N)
        mp = {} # <val, TreeNode>
        for u, v, is_left in descriptions:
            dsu.union(u, v)
            if u not in mp:
                mp[u] = TreeNode(u)
            if v not in mp:
                mp[v] = TreeNode(v)
            if is_left:
                mp[u].left = mp[v]
            else:
                mp[u].right = mp[v]
        root = dsu.find(descriptions[0][0])
        return mp[root]
    
class Solution2:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {} # val -> TreeNode
        pa = {} # child -> parent
        for u, v, is_left in descriptions:
            pa[v] = u
            if u not in mp:
                mp[u] = TreeNode(u)
            if v not in mp:
                mp[v] = TreeNode(v)
            if is_left:
                mp[u].left = mp[v]
            else:
                mp[u].right = mp[v]

        root = descriptions[0][0]
        while root in pa:
            root = pa[root]
        return mp[root]

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1],[2,3,0],[3,4,1]]\n
# @lcpr case=end

#

