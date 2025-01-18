#
# @lc app=leetcode id=3274 lang=python3
# @lcpr version=30204
#
# [3274] Check if Two Chessboard Squares Have the Same Color
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1, y1 = ord(coordinate1[0]) - ord('a'), int(coordinate1[1])
        x2, y2 = ord(coordinate2[0]) - ord('a'), int(coordinate2[1])
        return (x1 + y1) & 1 == (x2 + y2) & 1
# @lc code=end



#
# @lcpr case=start
# "a1"\n"c3"\n
# @lcpr case=end

# @lcpr case=start
# "a1"\n"h3"\n
# @lcpr case=end

#

