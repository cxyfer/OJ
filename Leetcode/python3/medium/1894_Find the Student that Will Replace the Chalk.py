#
# @lc app=leetcode id=1894 lang=python3
# @lcpr version=30204
#
# [1894] Find the Student that Will Replace the Chalk
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, x in enumerate(chalk):
            if k < x:
                return i
            k -= x
        return 0
    
class Solution2:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = list(accumulate(chalk))
        k %= s[-1]
        return bisect_right(s, k)
    
class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [5,1,5]\n22\n
# @lcpr case=end

# @lcpr case=start
# [3,4,1,2]\n25\n
# @lcpr case=end

#

