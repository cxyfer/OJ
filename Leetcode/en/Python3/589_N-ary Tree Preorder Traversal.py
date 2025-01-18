# @algorithm @lc id=775 lang=python3 
# @title n-ary-tree-preorder-traversal


from en.Python3.mod.preImport import *
# @test([1,null,3,2,4,null,5,6])=[1,3,5,6,2,4]
# @test([1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14])=[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            res = []
            if node is None:
                return res
            res = [node.val]
            for child in node.children:
                res += dfs(child)
            return res
        return dfs(root)