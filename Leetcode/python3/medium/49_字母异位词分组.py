#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from preImport import *
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for str in strs:
            cnt["".join(sorted(str))].append(str)
        return list(cnt.values())
# @lc code=end

