#
# @lc app=leetcode id=1100 lang=python3
#
# [1100] Find K-Length Substrings With No Repeated Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        ans = left = have = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            if cnt[ch] == 1:
                have += 1
            if right - left + 1 > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    have -= 1
                left += 1
            if have == k:
                ans += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.numKLenSubstrNoRepeats(s = "havefunonleetcode", k = 5))  # 6
print(sol.numKLenSubstrNoRepeats(s = "home", k = 5))  # 0
