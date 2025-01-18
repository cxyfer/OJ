#
# @lc app=leetcode id=2058 lang=python3
# @lcpr version=30204
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pre, cur = None, head
        first = last = -1
        mn = float('inf') # min distance
        idx = 0
        while cur and cur.next:
            if pre is not None and (pre.val < cur.val > cur.next.val or pre.val > cur.val < cur.next.val):
                if first == -1:
                    first = idx
                else:
                    mn = min(mn, idx - last)
                last = idx
            pre, cur = cur, cur.next
            idx += 1
        return [mn, last - first] if mn != float('inf') else [-1, -1]
# @lc code=end



#
# @lcpr case=start
# [3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,3,1,2,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,2,3,2,2,2,7]\n
# @lcpr case=end

#

