#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    """
        Two pointers
    """
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        lst = list(s)
        left = 0
        right = n - 1
        while left < right:
            while left < right and lst[left] not in "aeiouAEIOU":
                left += 1
            while left < right and lst[right] not in "aeiouAEIOU":
                right -= 1
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return "".join(lst)
# @lc code=end

