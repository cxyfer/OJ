#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root] if root else [])
        ans = []
        while q:
            ans.append(q[-1].val)
            for _ in range(len(q)):
                u = q.popleft()
                if u.left: q.append(u.left)
                if u.right: q.append(u.right)
        return ans
    
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans
    
# Solution = Solution1
Solution = Solution2
# @lc code=end

