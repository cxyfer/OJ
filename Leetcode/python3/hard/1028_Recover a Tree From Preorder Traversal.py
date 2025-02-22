#
# @lc app=leetcode.cn id=1028 lang=python3
# @lcpr version=30204
#
# [1028] 从先序遍历还原二叉树
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        st = []
        i = 0
        while i < n:
            # 計算深度，即 '-' 的數量
            lvl = 0
            while i < n and traversal[i] == '-':
                lvl += 1
                i += 1
            # 計算節點值
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            # 創建新節點
            node = TreeNode(val)
            
            # 如果堆疊不為空，則代表非根節點
            if st:
                # 調整堆疊大小，確保堆疊頂端節點為當前節點的父節點
                st = st[:lvl]
                # 根據題意，若一個節點有子節點，則先左子節點，再右子節點
                if not st[-1].left:
                    st[-1].left = node
                else:
                    st[-1].right = node
            # 將當前節點壓入堆疊
            st.append(node)
        # 返回根節點
        return st[0]
# @lc code=end

#
# @lcpr case=start
# "1-2--3--4-5--6--7"\n
# @lcpr case=end

# @lcpr case=start
# "1-2--3---4-5--6---7"\n
# @lcpr case=end

# @lcpr case=start
# "1-401--349---90--88"\n
# @lcpr case=end

#

