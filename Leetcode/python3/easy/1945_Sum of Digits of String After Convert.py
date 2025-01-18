#
# @lc app=leetcode id=1945 lang=python3
# @lcpr version=30204
#
# [1945] Sum of Digits of String After Convert
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0
        for ch in s:
            x = ord(ch) - ord('a') + 1
            while x > 0:
                ans += x % 10
                x //= 10
        for _ in range(k - 1):
            tmp = ans
            ans = 0
            while tmp > 0:
                ans += tmp % 10
                tmp //= 10
            if ans < 10:
                break
        return ans
# @lc code=end



#
# @lcpr case=start
# "iiii"\n1\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n2\n
# @lcpr case=end

# @lcpr case=start
# "zbax"\n2\n
# @lcpr case=end

#

