#
# @lc app=leetcode id=1506 lang=python3
#
# [1506] Find Root of N-Ary Tree
#


# @lcpr-template-start
from preImport import *
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
# @lcpr-template-end
# @lc code=start
class Solution1:
    def findRoot(self, tree: List["Node"]) -> "Node":
        ind = defaultdict(int)
        for u in tree:
            for v in u.children:
                ind[v.val] += 1
        for u in tree:
            if u.val not in ind:
                return u


class Solution2:
    def findRoot(self, tree: List["Node"]) -> "Node":
        xor = 0
        for u in tree:
            xor ^= u.val
            for v in u.children:
                xor ^= v.val
        for u in tree:
            if u.val == xor:
                return u


# Solution = Solution1
Solution = Solution2
# @lc code=end

