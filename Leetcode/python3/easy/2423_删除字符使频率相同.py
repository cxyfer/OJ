#
# @lc app=leetcode.cn id=2423 lang=python3
#
# [2423] 删除字符使频率相同
#
from preImport import *
# @lc code=start
class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = sorted(Counter(word).values()) # 出現次數由小到大排序
        # 1. 只有一種字母
        # 2. 只有一種字母出現一次，其他字母出現次數相同
        # 3. 只有一種字母出現次數最多，其他字母出現次數最多的字母次數比其他字母少一
        return len(cnt) == 1 or \
               cnt[0] == 1 and len(set(cnt[1:])) == 1 or \
               cnt[-1] == cnt[-2] + 1 and len(set(cnt[:-1])) == 1
# @lc code=end

sol = Solution()
print(sol.equalFrequency("abcc")) # true
print(sol.equalFrequency("aazz")) # false
print(sol.equalFrequency("bac")) # true
print(sol.equalFrequency("abbcc")) # true
