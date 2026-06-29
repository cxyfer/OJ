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
        need = 3
        ans = left = 0
        cnt = [0] * 3
        for right, ch in enumerate(s):
            c = ord(ch) - ord('a')
            # 1. 入窗口
            cnt[c] += 1
            if cnt[c] == 1:
                need -= 1
            # 2. 出窗口，維持窗口在向左延伸即可滿足條件的狀態
            while (need == 0):
                c = ord(s[left]) - ord('a')
                cnt[c] -= 1
                if cnt[c] == 0:
                    need += 1
                left += 1
            # 3. 累加答案，此時 [0, left - 1] 都是合法的左端點
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

