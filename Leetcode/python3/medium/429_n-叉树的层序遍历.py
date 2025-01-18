#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#
from preImport import *
# @lc code=start
# Definition for a Node.
class Solution:
    def levelOrder(self, root: 'SegmentTreeNode') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                for child in node.children:
                    q.append(child)
            ans.append(cur)
        return ans
# @lc code=end

