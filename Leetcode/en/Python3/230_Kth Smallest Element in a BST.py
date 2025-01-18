# @algorithm @lc id=230 lang=python3 
# @title kth-smallest-element-in-a-bst


from en.Python3.mod.preImport import *
# @test([3,1,4,null,2],1)=1
# @test([5,3,6,2,4,null,null,1],3)=3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        Inorder traversal
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = [] # Stack
        while st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

