#
# @lc app=leetcode.cn id=2975 lang=python3
#
# [2975] 移除栅栏得到的正方形田地的最大面积
#
from preImport import *
# @lc code=start
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # return self.solve1(m, n, hFences, vFences) 
        return self.solve2(m, n, hFences, vFences)
    """
        1. 賽時寫法，有點繞的寫法
    """
    def solve1(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()

        diff_h = [hFences[0]-1]
        diff_v = [vFences[0]-1]
        for i in range(1, len(hFences)):
            diff_h.append(hFences[i]-hFences[i-1])
        diff_h.append(m-hFences[-1])
        for i in range(1, len(vFences)):
            diff_v.append(vFences[i]-vFences[i-1])
        diff_v.append(n-vFences[-1])
        sum_h = list(accumulate(diff_h, initial=0))
        sum_v = list(accumulate(diff_v, initial=0))
        set_h = set(diff_h)
        set_v = set(diff_v)
        for i in range(1, len(sum_h)):
            for j in range(i):
                set_h.add(sum_h[i]-sum_h[j])
        for i in range(1, len(sum_v)):
            for j in range(i):
                set_v.add(sum_v[i]-sum_v[j])
        st = set_h.intersection(set_v)
        if not st:
            return -1
        max_width = max(st)
        return pow(max_width, 2, 10**9+7)
    def solve2(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def helper(fences: List[int], mx: int) -> Set[int]:
            fences.sort()
            fences = [1] + fences + [mx]
            res = set()
            for i in range(1, len(fences)):
                for j in range(i):
                    res.add(fences[i] - fences[j])
            return res
        h = helper(hFences, m)
        v = helper(vFences, n)
        intersection = h & v
        return pow(max(intersection), 2, 10**9+7) if intersection else -1
# @lc code=end

