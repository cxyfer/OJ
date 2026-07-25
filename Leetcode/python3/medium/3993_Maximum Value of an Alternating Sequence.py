#
# @lc app=leetcode id=3993 lang=python3
#
# [3993] Maximum Value of an Alternating Sequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Q2: 貪心
要構造最大的數可以在增加時 +m ，而減少時只 -1 。
增加次數最多為 n // 2 次，在最高值之前的減少次數為 max(0, n // 2 - 1) 次，因此可以直接計算出答案。
"""
# @lc code=start
class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        return s + m * (n // 2) - max(0, n // 2 - 1)
# @lc code=end

