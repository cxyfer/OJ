#
# @lc app=leetcode id=2181 lang=python3
# @lcpr version=30204
#
# [2181] Merge Nodes in Between Zeros
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: # for pylance
            return None
        pre = head # previous 0 node
        cur = head.next
        s = 0
        while cur:
            if cur.val == 0:
                cur.val = s
                s = 0
                pre.next = cur # connect the previous 0 node to the current node
                pre = cur
            else:
                s += cur.val
            cur = cur.next
        return head.next # the first 0 node is not needed
# @lc code=end



#
# @lcpr case=start
# [0,3,1,0,4,5,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,0,2,2,0]\n
# @lcpr case=end

#

