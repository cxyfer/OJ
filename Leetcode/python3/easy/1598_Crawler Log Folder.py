#
# @lc app=leetcode id=1598 lang=python3
# @lcpr version=30204
#
# [1598] Crawler Log Folder
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                ans = max(ans - 1, 0)
            else:
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# ["d1/","d2/","../","d21/","./"]\n
# @lcpr case=end

# @lcpr case=start
# ["d1/","d2/","./","d3/","../","d31/"]\n
# @lcpr case=end

# @lcpr case=start
# ["d1/","../","../","../"]\n
# @lcpr case=end

#

