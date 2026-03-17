#
# @lc app=leetcode id=1727 lang=python3
#
# [1727] Largest Submatrix With Rearrangements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
枚舉每個底邊，則只需關注每個 col 的底邊上有幾個 1 即可。
由於可以交換，故可以將 col 從大到小（或從小到大）排序，計算可組成的最大矩形面積。

排序可以用以下想法優化掉：
因為每次掃到新的橫列時，值只會「+1」或「變成 0」，
而 +1 的部分相對順序是不變的，因此其實只需要把變成 0 的下標抽出來即可。
"""
class Solution1:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        ans = 0
        cols = [0] * n
        for row in matrix:
            for j, val in enumerate(row):
                if val == 1:
                    cols[j] += 1
                else:
                    cols[j] = 0
            for j, h in enumerate(sorted(cols, reverse=True), start=1):
                if h == 0:
                    break
                ans = max(ans, h * j)
        return ans

class Solution2:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        ans = 0
        cols = [0] * len(matrix[0])
        idxs = list(range(n))
        for row in matrix:
            arr1, arr2 = [], []
            for idx in idxs:
                if row[idx] == 1:
                    cols[idx] += 1
                    arr1.append(idx)
                else:
                    cols[idx] = 0
                    arr2.append(idx)
            idxs = arr1 + arr2
            for j, idx in enumerate(idxs, start=1):
                if cols[idx] == 0:
                    break
                ans = max(ans, cols[idx] * j)
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end
sol = Solution()
print(sol.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))  # 4