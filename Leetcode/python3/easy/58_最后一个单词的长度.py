#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split(' ')[-1])
        ans = cur = 0
        for ch in s:
            if ch == ' ':
                ans = cur if cur != 0 else ans
                cur = 0
            else:
                cur += 1
        return cur if cur != 0 else ans
# @lc code=end

