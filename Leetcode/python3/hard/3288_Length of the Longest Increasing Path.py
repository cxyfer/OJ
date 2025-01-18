#
# @lc app=leetcode id=3288 lang=python3
# @lcpr version=30204
#
# [3288] Length of the Longest Increasing Path
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        2D LIS
    """
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        target = coordinates[k]
        c1, c2 = [], []
        for x, y in coordinates:
            if x < target[0] and y < target[1]:
                c1.append((x, y))
            elif x > target[0] and y > target[1]:
                c2.append((x, y))
        """
            這裡要注意，如果 x 相同，y 要由大到小排序
            這樣才能保證我們在計算 x 的 LIS 時，相同的 y 最多選 1 個 x
        """
        c1.sort(key = lambda x: (x[0], -x[1])) 
        c2.sort(key = lambda x: (x[0], -x[1]))
        # print(target, c1, c2, sep = "\n")
        def LIS(arr):
            n = len(arr)
            if n == 0:
                return 0
            # 令 tail[i] 表示長度為 i + 1 的 LIS 的最小結尾元素
            tail = [arr[0]]
            for i in range(1, n):
                # arr[i] 可以接在 tail[-1] 後面，構成更長的 LIS
                if arr[i][0] > tail[-1][0] and arr[i][1] > tail[-1][1]:
                    tail.append(arr[i])
                    continue
                # 如果 arr[i] 不能接在 tail[-1] 後面，則需要找到 arr[i] 可以插入的位置
                left, right = 0, len(tail) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if tail[mid][0] < arr[i][0] and tail[mid][1] < arr[i][1]:
                        left = mid + 1
                    else:
                        right = mid - 1
                tail[left] = arr[i]
            return len(tail)
        return LIS(c1) + 1 + LIS(c2)
# @lc code=end

sol = Solution()
print(sol.maxPathLength([[3,1],[2,2],[4,1],[0,0],[5,3]], 1)) # 3
print(sol.maxPathLength([[2,1],[7,0],[5,6]], 2)) # 2
print(sol.maxPathLength([[7,6],[5,8],[4,6],[4,3],[6,4]], 3)) # 3
print(sol.maxPathLength([[9,6],[8,3],[3,2],[3,5]], 0)) # 3

#
# @lcpr case=start
# [[3,1],[2,2],[4,1],[0,0],[5,3]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[2,1],[7,0],[5,6]]\n2\n
# @lcpr case=end

#

