#
# @lc app=leetcode id=2096 lang=python3
# @lcpr version=30204
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
    1. DFS建圖 + 從起點開始DFS
    2. LCA
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        g = defaultdict(list)
        def dfs1(u: TreeNode, fa: int):
            if u.left is not None:
                g[u.val].append((u.left.val, "L"))
                g[u.left.val].append((u.val, "U"))
                dfs1(u.left, u.val)
            if u.right is not None:
                g[u.val].append((u.right.val, "R"))
                g[u.right.val].append((u.val, "U"))
                dfs1(u.right, u.val)

        dfs1(root, -1)
        ans = ""
        path = []
        def dfs2(u: int, fa: int):
            if u == destValue:
                nonlocal ans
                ans = "".join(path)
                return True
            for v, d in g[u]:
                if v == fa:
                    continue
                path.append(d)
                if dfs2(v, u):
                    return True
                path.pop()
            return False
        dfs2(startValue, -1)
        return ans
# @lc code=end



#
# @lcpr case=start
# [5,1,2,3,null,6,4]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n1\n
# @lcpr case=end

#

