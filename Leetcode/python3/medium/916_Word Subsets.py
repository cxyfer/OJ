#
# @lc app=leetcode id=916 lang=python3
# @lcpr version=30204
#
# [916] Word Subsets
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt2 = Counter()
        for w in words2:
            cnt = Counter(w)
            for ch in cnt:
                cnt2[ch] = max(cnt2[ch], cnt[ch])
        ans = []
        for w in words1:
            cnt_w = Counter(w)
            if all(cnt_w[ch] >= cnt2[ch] for ch in cnt2):
                ans.append(w)
        return ans
# @lc code=end

sol = Solution()
print(sol.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))

#
# @lcpr case=start
# ["amazon","apple","facebook","google","leetcode"]\n["e","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["amazon","apple","facebook","google","leetcode"]\n["l","e"]\n
# @lcpr case=end

#

