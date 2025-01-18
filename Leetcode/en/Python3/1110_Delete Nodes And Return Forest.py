# @algorithm @lc id=1207 lang=python3 
# @title delete-nodes-and-return-forest


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5,6,7],[3,5])=[[1,2,null,4],[6],[7]]
# @test([1,2,4,null,3],[3])=[[1,2,4]]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)
        def dfs(root: Optional[TreeNode], isRoot: bool) -> Optional[TreeNode]:
            if not root: return None
            if root.val in to_delete: # 把左右子樹視為新的根節點
                dfs(root.left, True) #  遞迴處理左右子樹
                dfs(root.right, True) 
                return None # 刪除自己
            else:
                if isRoot: ans.append(root) # 如果是根節點，加入森林
                root.left = dfs(root.left, False) # 遞迴處理左右子樹
                root.right = dfs(root.right, False)
                return root
        dfs(root, True)
        return ans