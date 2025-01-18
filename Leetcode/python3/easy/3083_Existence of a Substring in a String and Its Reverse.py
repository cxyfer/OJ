#
# @lc app=leetcode id=3083 lang=python3
# @lcpr version=30204
#
# [3083] Existence of a Substring in a String and Its Reverse
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        st = set()
        for x, y in pairwise(s):
            st.add(x + y)
            if y + x in st:
                return True
        return False
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

# @lcpr case=start
# "abcba"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n
# @lcpr case=end

#

