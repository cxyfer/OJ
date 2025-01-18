#
# @lc app=leetcode.cn id=2586 lang=python3
#
# [2586] 统计范围内的元音字符串数
#
from preImport import *
# @lc code=start
class Solution:
    VOWEL = ['a','e','i','o','u']
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum([word[0] in self.VOWEL and word[-1] in self.VOWEL for word in words[left:right+1]])
# @lc code=end
sol = Solution()
print(sol.vowelStrings(["are","amy","u"],0,2))  # 2

