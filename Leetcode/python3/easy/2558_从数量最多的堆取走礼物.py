#
# @lc app=leetcode.cn id=2558 lang=python3
#
# [2558] 从数量最多的堆取走礼物
#
from preImport import *
# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        lst = SortedList(gifts)
        for i in range(k):
            lst.add(isqrt(lst.pop()))
        return sum(lst)
# @lc code=end

