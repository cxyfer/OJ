#
# @lc app=leetcode id=2710 lang=python3
# @lcpr version=30204
#
# [2710] Remove Trailing Zeros From a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # return num.rstrip('0')
        lst = list(num)
        while lst[-1] == '0':
            lst.pop()
        return ''.join(lst)
# @lc code=end



#
# @lcpr case=start
# "51230100"\n
# @lcpr case=end

# @lcpr case=start
# "123"\n
# @lcpr case=end

#

