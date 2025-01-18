# @algorithm @lc id=2571 lang=python3 
# @title find-the-pivot-integer


from en.Python3.mod.preImport import *
# @test(8)=6
# @test(1)=1
# @test(4)=-1
class Solution:
    """
        1. Binary search
        2. Math
    """
    def pivotInteger(self, n: int) -> int:
        # return self.solve1(n)
        return self.solve2(n)
    def solve1(self, n: int) -> int:
        s = (1 + n) * n // 2
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            s1 = (1 + mid) * mid // 2
            s2 = s - s1 + mid
            if s1 == s2:
                return mid
            elif s1 < s2:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    def solve2(self, n: int) -> int:
        s = n * (n + 1) // 2
        x = math.isqrt(s)
        return x if x * x == s else -1