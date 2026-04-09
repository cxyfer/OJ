#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        def dfs(left: int, right: int) -> int:
            if left == right:
                return 0
            mid = (left + right) // 2
            res = dfs(left, mid) + dfs(mid + 1, right)

            # 在兩個**有序**陣列上，計算 s[j] - s[i] 在 [lower, upper] 之間的數量
            # r1 是第一個 >= s[i] + lower 的下標；r2 是第一個 > s[i] + upper 的下標
            r1 = r2 = mid + 1
            for i in range(left, mid + 1):
                while r1 <= right and s[r1] - s[i] < lower:
                    r1 += 1
                while r2 <= right and s[r2] - s[i] <= upper:
                    r2 += 1
                res += r2 - r1

            # 用 Merge sort 方式保持陣列有序
            tmp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if s[i] < s[j]:
                    tmp.append(s[i])
                    i += 1
                else:
                    tmp.append(s[j])
                    j += 1
            tmp.extend(s[i:mid + 1])
            tmp.extend(s[j:right + 1])
            s[left : right + 1] = tmp
            return res

        return dfs(0, n)
# @lc code=end

sol = Solution()
print(sol.countRangeSum([-2,5,-1], -2, 2)) # 3
print(sol.countRangeSum([0], 0, 0)) # 1
