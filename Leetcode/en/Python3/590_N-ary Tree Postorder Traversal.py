# @algorithm @lc id=776 lang=python3 
# @title n-ary-tree-postorder-traversal


from en.Python3.mod.preImport import *
# @test([1,null,3,2,4,null,5,6])=[5,6,3,2,4,1]
# @test([1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14])=[2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            res = []
            if node is None:
                return res
            res = []
            for child in node.children:
                res += dfs(child)
            res.append(node.val)
            return res
        return dfs(root)