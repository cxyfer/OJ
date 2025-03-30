#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, x = q.popleft()
            if node:
                ans[x].append(node.val)
                q.append((node.left, x - 1))
                q.append((node.right, x + 1))
        return [ans[x] for x in sorted(ans)]
# @lc code=end

