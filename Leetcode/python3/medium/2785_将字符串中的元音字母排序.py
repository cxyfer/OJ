#
# @lc app=leetcode.cn id=2785 lang=python3
#
# [2785] 将字符串中的元音字母排序
#

# @lc code=start
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted([ch for ch in s if ch in "AEIOUaeiou"], reverse = True)
        return ''.join(vowels.pop() if ch in "AEIOUaeiou" else ch for ch in s)
# @lc code=end

