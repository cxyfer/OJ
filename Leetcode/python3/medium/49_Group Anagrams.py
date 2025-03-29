#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans["".join(sorted(s))].append(s)
        return list(ans.values())
# @lc code=end

