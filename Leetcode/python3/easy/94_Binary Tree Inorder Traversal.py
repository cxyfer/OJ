#
# @lc app=leetcode id=94 lang=python3
# @lcpr version=30201
#
# [94] Binary Tree Inorder Traversal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Recursion
        2. Iteration + Stack
        3. Morris Traversal
            SC: O(1)
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.solve1(root)
        # return self.solve2(root)
        return self.solve3(root)
    def solve1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    def solve2(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []
        cur = root
        while (cur or st):
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
    def solve3(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        pre = None # predecessor 前驅節點，即左子樹中的最右節點
        while root:
            if root.left: # 存在左子樹
                pre = root.left
                while pre.right and pre.right != root: # 找到左子樹中的最右節點
                    pre = pre.right
                if not pre.right: # 左子樹還沒有被訪問過，遍歷左子樹
                    pre.right = root
                    root = root.left
                else: # 左子樹已經訪問過，可以訪問當前節點了，並斷開 pre 指向 root 的指標
                    ans.append(root.val)
                    pre.right = None # 斷開
                    root = root.right
            else: # 不存在左子樹，直接訪問右子樹
                ans.append(root.val)
                root = root.right
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

