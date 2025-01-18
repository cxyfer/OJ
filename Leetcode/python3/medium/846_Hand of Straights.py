#
# @lc app=leetcode id=846 lang=python3
# @lcpr version=30203
#
# [846] Hand of Straights
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Same as 1296\. Divide Array in Sets of K Consecutive Numbers
    """
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        for k in sorted(cnt.keys()):
            if cnt[k] == 0:
                continue
            need = cnt[k]
            for i in range(groupSize):
                if cnt[k+i] < need:
                    return False
                cnt[k+i] -= need
        return True
# @lc code=end

[1]
1




#
# @lcpr case=start
# [1,2,3,6,2,3,4,7,8]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n4\n
# @lcpr case=end

#

