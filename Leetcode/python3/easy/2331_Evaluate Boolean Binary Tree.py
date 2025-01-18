#
# @lc app=leetcode id=2331 lang=python3
# @lcpr version=30202
#
# [2331] Evaluate Boolean Binary Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """ 遞迴(Recursion)
        由於 AND / OR 都是 Binary Operator，所以這是一棵Full Binary Tree，
        也就是除了樹葉以外，每個節點都有兩個child，在判斷是否為Leaf時只要判斷一邊就好。
        此外，由於可能可以提前短路，所以不用先計算左右子樹的值。
    """
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # if not root.left and not root.right: # if leaf node
        if not root.left: # 只要判斷一邊就好
            return root.val == 1
        if root.val == 3: # 由於可能可以提前短路，所以不用先計算左右子樹的值
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
# @lc code=end



#
# @lcpr case=start
# [2,1,3,null,null,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

