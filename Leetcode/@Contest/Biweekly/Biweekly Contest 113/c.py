# 6988. 统计距离为 k 的点对 显示英文描述 

# 给你一个 二维 整数数组 coordinates 和一个整数 k ，其中 coordinates[i] = [xi, yi] 是第 i 个点在二维平面里的坐标。

# 我们定义两个点 (x1, y1) 和 (x2, y2) 的 距离 为 (x1 XOR x2) + (y1 XOR y2) ，XOR 指的是按位异或运算。

# 请你返回满足 i < j 且点 i 和点 j之间距离为 k 的点对数目。

from collections import Counter
from typing import List

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        """
            1. 暴力(超時)
        """
        # n = len(coordinates)
        # ans = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         x1, y1 = coordinates[i]
        #         x2, y2 = coordinates[j]
        #         if (x1 ^ x2) + (y1 ^ y2) == k:
        #             ans += 1
        # return ans
        """
            2. Brute Force + Hash Table
            (x1 ^ x2) + (y1 ^ y2) = k
            0 <= (x1 ^ x2) <= k
            0 <= (y1 ^ y2) <= k
            x1 ^ x2 = i
            y1 ^ y2 = k - i
            => x1 ^ x2 ^ x2 = i ^ x2 => x1 = i ^ x2
        """
        ans = 0
        cnt = Counter()
        for x1, y1 in coordinates:
            for i in range(k+1):
                ans += cnt[(x1 ^ i, y1 ^ (k - i))]
            cnt[(x1, y1)] += 1
        return ans  