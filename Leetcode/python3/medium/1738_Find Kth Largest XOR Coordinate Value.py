#
# @lc app=leetcode id=1738 lang=python3
# @lcpr version=30202
#
# [1738] Find Kth Largest XOR Coordinate Value
#


# @lcpr-template-start
from re import S

from preImport import *
# @lcpr-template-end
"""
二維前綴異或和 + Sort/Heap
"""
# @lc code=start
class Solution1:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]  # Prefix Sum
        res = []
        for i, row in enumerate(matrix, start=1):
            for j, val in enumerate(row, start=1):
                s[i][j] = s[i - 1][j] ^ s[i][j - 1] ^ s[i - 1][j - 1] ^ val
                res.append(s[i][j])
        res.sort(reverse=True)
        return res[k - 1]


class Solution2:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]  # Prefix Sum
        hp = []  # Min Heap
        for i, row in enumerate(matrix, start=1):
            for j, val in enumerate(row, start=1):
                s[i][j] = s[i - 1][j] ^ s[i][j - 1] ^ s[i - 1][j - 1] ^ val
                if len(hp) < k:
                    heappush(hp, s[i][j])
                else:
                    heappushpop(hp, s[i][j])
        return hp[0]


# Solution = Solution1
Solution = Solution2
# @lc code=end
sol = Solution()
print(sol.kthLargestValue([[5,2],[1,6]], 1)) # 7
print(sol.kthLargestValue([[5,2],[1,6]], 2)) # 5
print(sol.kthLargestValue([[5,2],[1,6]], 3)) # 4


#
# @lcpr case=start
# [[5,2],[1,6]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[5,2],[1,6]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[5,2],[1,6]]\n3\n
# @lcpr case=end

#

