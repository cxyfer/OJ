#
# @lc app=leetcode id=1408 lang=python3
# @lcpr version=30204
#
# [1408] String Matching in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for w1 in words:
            for w2 in words:
                if w1 in w2 and w1 != w2:
                    ans.append(w1)
                    break
        return ans
# @lc code=end



#
# @lcpr case=start
# ["mass","as","hero","superhero"]\n
# @lcpr case=end

# @lcpr case=start
# ["leetcode","et","code"]\n
# @lcpr case=end

# @lcpr case=start
# ["blue","green","bu"]\n
# @lcpr case=end

#

