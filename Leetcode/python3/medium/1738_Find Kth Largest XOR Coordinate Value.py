#
# @lc app=leetcode id=1738 lang=python3
# @lcpr version=30202
#
# [1738] Find Kth Largest XOR Coordinate Value
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        二維前綴異或和 + Sort/Heap
    """
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # return self.solve1(matrix, k)
        return self.solve2(matrix, k)
    def solve1(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)] # Prefix Sum
        res = []
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                pre[i+1][j+1] = pre[i+1][j] ^ pre[i][j+1] ^ pre[i][j] ^ val
                res.append(pre[i+1][j+1])
        res.sort(reverse=True)
        return res[k-1]
    def solve2(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)] # Prefix Sum
        hp = [] # Min Heap
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                pre[i+1][j+1] = pre[i+1][j] ^ pre[i][j+1] ^ pre[i][j] ^ val
                if len(hp) < k:
                    heappush(hp, pre[i+1][j+1])
                else:
                    heappushpop(hp, pre[i+1][j+1])
        return hp[0]
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

