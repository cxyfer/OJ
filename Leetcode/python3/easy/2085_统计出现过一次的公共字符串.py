#
# @lc app=leetcode.cn id=2085 lang=python3
#
# [2085] 统计出现过一次的公共字符串
#
from preImport import *
# @lc code=start
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        cnt = Counter()
        for k, v in cnt1.items():
            if v == 1:
                cnt[k] += 1
        for k, v in cnt2.items():
            if v == 1:
                cnt[k] += 1
        return len([k for k, v in cnt.items() if v == 2])
# @lc code=end
sol = Solution()
print(sol.countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"])) # 2