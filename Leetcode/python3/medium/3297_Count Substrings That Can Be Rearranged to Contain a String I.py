#
# @lc app=leetcode id=3297 lang=python3
# @lcpr version=30204
#
# [3297] Count Substrings That Can Be Rearranged to Contain a String I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt = Counter(word2) # 需要的字元數量
        need = len(cnt) # 需要的字元種類數
        ans = left = have = 0
        for right, ch in enumerate(word1):
            cnt[ch] -= 1
            if cnt[ch] == 0: # 這個字元的數量夠了
                have += 1
            while left <= right and have == need: # 當前窗口已經滿足需求，縮小窗口
                cnt[word1[left]] += 1
                if cnt[word1[left]] == 1: # 這個字元的數量變回不夠
                    have -= 1
                left += 1
            ans += left # [0, right], [1, right], [2, right], ..., [left - 1, right] 都是符合條件的子字串
        return ans
# @lc code=end

sol = Solution()
print(sol.validSubstringCount("bcca", "abc")) # 1
print(sol.validSubstringCount("abcabc", "abc")) # 10
print(sol.validSubstringCount("abcabc", "aaabc")) # 0

#
# @lcpr case=start
# "bcca"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abcabc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abcabc"\n"aaabc"\n
# @lcpr case=end

#

