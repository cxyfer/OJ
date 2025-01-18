#
# @lc app=leetcode id=1358 lang=python3
# @lcpr version=30204
#
# [1358] Number of Substrings Containing All Three Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = left = have = 0
        cnt = defaultdict(int)
        for ch in s:
            cnt[ch] += 1
            if cnt[ch] == 1:
                have += 1
            while (have == 3):
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    have -= 1
                left += 1
            ans += left
        return ans
# @lc code=end

sol = Solution()
print(sol.numberOfSubstrings("abcabc")) # 10
print(sol.numberOfSubstrings("aaacb")) # 3
print(sol.numberOfSubstrings("abc")) # 1


#
# @lcpr case=start
# "abcabc"\n
# @lcpr case=end

# @lcpr case=start
# "aaacb"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

