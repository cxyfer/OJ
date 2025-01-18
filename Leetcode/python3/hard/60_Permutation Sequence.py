#
# @lc app=leetcode id=60 lang=python3
# @lcpr version=30203
#
# [60] Permutation Sequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = list(range(1, n+1))
        k -= 1
        ans = []
        while len(s) > 0:
            x = math.factorial(len(s)-1)
            i = k // x
            ans.append(s[i])
            s = s[:i] + s[i+1:]
            k %= x
        return "".join(map(str, ans))
# @lc code=end



#
# @lcpr case=start
# 3\n3\n
# @lcpr case=end

# @lcpr case=start
# 4\n9\n
# @lcpr case=end

# @lcpr case=start
# 3\n1\n
# @lcpr case=end

#

