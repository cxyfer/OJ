#
# @lc app=leetcode id=2678 lang=python3
# @lcpr version=30204
#
# [2678] Number of Senior Citizens
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # return sum(int(detail[11:13]) > 60 for detail in details)
        ans = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# ["7868190130M7522","5303914400F9211","9273338290F4010"]\n
# @lcpr case=end

# @lcpr case=start
# ["1313579440F2036","2921522980M5644"]\n
# @lcpr case=end

#

