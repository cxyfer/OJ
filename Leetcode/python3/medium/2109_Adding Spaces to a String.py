#
# @lc app=leetcode id=2109 lang=python3
# @lcpr version=30204
#
# [2109] Adding Spaces to a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        pre = 0 
        for i in spaces:
            res.append(s[pre:i])
            pre = i
        res.append(s[pre:])
        return ' '.join(res)
# @lc code=end



#
# @lcpr case=start
# "LeetcodeHelpsMeLearn"\n[8,13,15]\n
# @lcpr case=end

# @lcpr case=start
# "icodeinpython"\n[1,5,7,9]\n
# @lcpr case=end

# @lcpr case=start
# "spacing"\n[0,1,2,3,4,5,6]\n
# @lcpr case=end

#

