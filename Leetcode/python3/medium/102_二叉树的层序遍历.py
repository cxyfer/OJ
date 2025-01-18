#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
from preImport import *
# @lc code=start
class Solution:
    """
        Level order traversal
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return ans
        q = deque([root])
        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(cur)
        return ans
# @lc code=end

