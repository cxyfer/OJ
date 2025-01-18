#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
from preImport import *
# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        return self.solve2(points)
    """
        1. Brute Force
        Time: O(n^3)
    """
    def solve1(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 1
        for i, x in enumerate(points):
            for j in range(i + 1, n): # 以 x, y 為兩點的直線上有多少點
                y = points[j]
                cnt = 2
                for k in range(j + 1, n):
                    z = points[k]
                    # (y[1] - x[1]) / (y[0] - x[0]) == (z[1] - y[1]) / (z[0] - y[0])
                    if (y[1] - x[1]) * (z[0] - y[0]) == (z[1] - y[1]) * (y[0] - x[0]):
                        cnt += 1
                ans = max(ans, cnt)
        return ans
    """
        2. Hash Table
        Time: O(n^2)
        用math.gcd()一律會返回正數，要處理負數的情況
    """
    def solve2(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        n = len(points)
        ans = 1
        for i in range(n):
            cnt = defaultdict(int)
            maxv = 0
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                a, b = x1 - x2, y1 - y2
                k = math.gcd(a, b)
                # if k != math.gcd(a, b):
                #     print(a, b, k, math.gcd(a, b))
                key = (a // k, b // k)
                if key[0] < 0 and key[1] < 0:
                    key = (-key[0], -key[1])
                elif key[0] < 0: # 確保 key[0] 是正的
                    key = (-key[0], -key[1])
                if key[0] == 0 and key[1] < 0 or key[0] < 0 and key[1] == 0:
                    key = (-key[0], -key[1])
                cnt[key] += 1
                maxv = max(maxv, cnt[key])
            ans = max(ans, maxv + 1)    
        return ans
# @lc code=end
sol = Solution()
print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])) # 4
print(sol.maxPoints([[0,1],[0,0],[0,4],[0,-2],[0,-1],[0,3],[0,-4]])) # 7
print(math.gcd(-15, 5))