#
# @lc app=leetcode id=3325 lang=python3
# @lcpr version=30204
#
# [3325] Count Substrings With K-Frequency Characters I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Sliding Window: 求子陣列個數 - 越長越合法
"""
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] >= k:
                cnt[s[left]] -= 1
                left += 1
            ans += left
        return ans
# @lc code=end

sol = Solution()
print(sol.numberOfSubstrings("abacb", 2))

#
# @lcpr case=start
# "abacb"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n1\n
# @lcpr case=end

#

