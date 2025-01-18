#
# @lc app=leetcode.cn id=1261 lang=python3
#
# [1261] 在受污染的二叉树中查找元素
#
from preImport import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements1:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.vals = set([0])
        def dfs(node: TreeNode, val: int):
            if node.left:
                node.left.val = 2 * val + 1
                self.vals.add(node.left.val)
                dfs(node.left, node.left.val)
            if node.right:
                node.right.val = 2 * val + 2
                self.vals.add(node.right.val)
                dfs(node.right, node.right.val)
        dfs(self.root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals
    
class FindElements2:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        target += 1 # 由於將所有節點的值加1，所以查找的值也要加1
        cur = self.root  
        for i in range(target.bit_length() - 2, -1, -1): # 從第二位開始，因為第一位必定是1
            b = target & (1 << i) # 取出第i位的值
            cur = cur.right if b else cur.left # 如果第i位是1，就往右走，否則往左走
            if cur is None: # 走到空節點，說明目標值存在，返回False
                return False
        return True

class FindElements(FindElements2):
    pass

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

