#
# @lc app=leetcode id=1846 lang=python3
#
# [1846] Maximum Element After Decreasing and Rearranging
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        arr[0] = 1
        for i in range(1, n):
            arr[i] = min(arr[i], arr[i - 1] + 1)
        return arr[-1]


class Solution2:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [0] * (n + 1)

        for x in arr:
            cnt[min(x, n)] += 1

        ans = 0
        for v in range(1, n + 1):
            ans = min(v, ans + cnt[v])
        return ans


Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))  # Output: 2
print(sol.maximumElementAfterDecrementingAndRearranging([100,1,1000]))  # Output: 3
print(sol.maximumElementAfterDecrementingAndRearranging([1,2,3,4,5]))  # Output: 5