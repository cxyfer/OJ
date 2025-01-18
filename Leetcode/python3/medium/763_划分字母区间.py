#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from preImport import *
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i, ch in enumerate(s):
            last[ch] = i
        
        ans = []
        st = ed = 0
        for i, ch in enumerate(s):
            ed = max(ed, last[ch])
            if i == ed:
                ans.append(ed - st + 1)
                st = ed + 1
        return ans
# @lc code=end

