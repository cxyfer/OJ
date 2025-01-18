# @algorithm @lc id=235 lang=python3 
# @title lowest-common-ancestor-of-a-binary-search-tree


from en.Python3.mod.preImport import *
# @test([6,2,8,0,4,7,9,null,null,3,5],2,8)=6
# @test([6,2,8,0,4,7,9,null,null,3,5],2,4)=2
# @test([2,1],2,1)=2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        Similar to 236. Lowest Common Ancestor of a Binary Tree
        與 236. 類似的討論方式，若 root 是 p, q 的 最近共同祖先，則只可能為以下情況之一：
            1. p 和 q 分別在 root 的 左/右子樹中
            2. p = root，且 q 在 root 的 左/右子樹中
            3. q = root，且 p 在 root 的 左/右子樹中
        由於這題是BST，所以可以由大小關係來簡化判斷
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val: # p 和 q 都在左子樹中
            return self.lowestCommonAncestor(root.left, p, q) 
        elif p.val > root.val and q.val > root.val: # p 和 q 都在右子樹中
            return self.lowestCommonAncestor(root.right, p, q)
        else: # p 和 q 分別在 root 的 左/右子樹中，或是p 和 q 其中一個是 root
            return root 