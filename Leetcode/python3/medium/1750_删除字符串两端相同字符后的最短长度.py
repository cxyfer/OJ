#
# @lc app=leetcode.cn id=1750 lang=python3
#
# [1750] 删除字符串两端相同字符后的最短长度
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        left, right = 0, n - 1
        while left < right and s[left] == s[right]: # 存在由相同字元構成的前綴和後綴
            ch = s[left]
            while left <= right and s[left] == ch: # 刪除由 ch 構成的前綴
                left += 1
            while left <= right and s[right] == ch: # 刪除由 ch 構成的後綴
                right -= 1
        return right - left + 1
# @lc code=end

