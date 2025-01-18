# @algorithm @lc id=1295 lang=python3 
# @title minimum-garden-perimeter-to-collect-enough-apples


from en.Python3.mod.preImport import *
# @test(1)=8
# @test(13)=16
# @test(1000000000)=5040
class Solution:
    """
        Math + Binary Search
        推出每層的蘋果數量為 12 * n^2 
        故前 n 層的蘋果數量為 12 * n * (n + 1) * (2 * n + 1) / 6 = 2 * n * (n + 1) * (2 * n + 1)
        二分答案即可，每層的邊長為 8 * n
    """
    def minimumPerimeter(self, neededApples: int) -> int:
        def calc(n): # 計算前 n 層的蘋果數量
            return 2 * n * (n + 1) * (2 * n + 1)
        left, right = 0, 10 ** 5
        while (left <= right):
            mid = (left + right) // 2
            if calc(mid) >= neededApples:
                right = mid - 1
            else:
                left = mid + 1
        return 8 * left # 每層的邊長為 8 * n