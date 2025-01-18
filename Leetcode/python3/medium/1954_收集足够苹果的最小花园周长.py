#
# @lc app=leetcode.cn id=1954 lang=python3
#
# [1954] 收集足够苹果的最小花园周长
#

# @lc code=start
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

# @lc code=end

