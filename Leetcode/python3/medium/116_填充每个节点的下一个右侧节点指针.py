#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
from preImport import *
# @lc code=start
# Definition for a Node.
class SegmentTreeNode:
    def __init__(self, val: int = 0, left: 'SegmentTreeNode' = None, right: 'SegmentTreeNode' = None, next: 'SegmentTreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    """
        Level order
    """
    def connect(self, root: 'SegmentTreeNode') -> 'SegmentTreeNode':
        if not root:
            return root
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
# @lc code=end

