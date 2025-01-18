# @algorithm @lc id=606 lang=python3 
# @title construct-string-from-binary-tree


from en.Python3.mod.preImport import *
# @test([1,2,3,4])="1(2(4))(3)"
# @test([1,2,3,null,4])="1(2()(4))(3)"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        若左子樹不為空、右子樹為空，可以省略右子樹的括號
        若左子樹為空、右子樹不為空，左子樹的括號不能省略
    """
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preOrder(root):
            if not root:
                return ''
            if not root.left and not root.right: # 左右子樹都為空
                return f"{root.val}"
            elif not root.right: # 左子樹不為空、右子樹為空
                return f"{ root.val }({ preOrder(root.left) })"
            else: # 左子樹為空、右子樹不為空 / 左右子樹都不為空
                return f"{ root.val }({ preOrder(root.left) })({ preOrder(root.right) })"
        return preOrder(root)