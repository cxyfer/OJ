#
# @lc app=leetcode id=2347 lang=python3
# @lcpr version=30201
#
# [2347] Best Poker Hand
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        s = len(set(suits))
        r = max(Counter(ranks).values())
        if s == 1:
            return "Flush"
        if r >= 3:
            return "Three of a Kind"
        if r == 2:
            return "Pair"
        return "High Card"
# @lc code=end



#
# @lcpr case=start
# [13,2,3,1,9]\n["a","a","a","a","a"]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,2,4,4]\n["d","a","a","b","c"]\n
# @lcpr case=end

# @lcpr case=start
# [10,10,2,12,9]\n["a","b","c","a","d"]\n
# @lcpr case=end

#

