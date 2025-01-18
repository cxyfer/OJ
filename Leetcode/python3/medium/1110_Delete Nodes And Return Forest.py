#
# @lc app=leetcode id=1110 lang=python3
# @lcpr version=30204
#
# [1110] Delete Nodes And Return Forest
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete_set = set(to_delete)
        def dfs(root: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not root:
                return None
            if root.val in to_delete_set:  # 把左右子樹視為新的根節點
                dfs(root.left, True)  # 遞迴處理左右子樹
                dfs(root.right, True)
                return None  # 刪除自己
            else:
                if is_root: # 如果是根節點，加入答案
                    ans.append(root)  
                root.left = dfs(root.left, False)  # 遞迴處理左右子樹
                root.right = dfs(root.right, False)
                return root
        dfs(root, True)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n[3,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,null,3]\n[3]\n
# @lcpr case=end

#

