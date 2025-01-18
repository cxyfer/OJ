#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
            Backtrace, similar to 46.Permutations.
        """
        ans = []
        res = []
        def backtrace(i: int, avail: List[int]) -> None:
            if i == k:
                if sum(res) == n:
                    ans.append(res.copy())
                return
            for num in avail:
                res.append(num)
                # 這裡要過濾掉比num小的數字，因為這樣才能保證不重複
                backtrace(i + 1, [x for x in avail if x > num]) 
                res.pop()
        backtrace(0, list(range(1, 10)))
        return ans
# @lc code=end

sol = Solution()
print(sol.combinationSum3(3, 7))
print(sol.combinationSum3(3, 9))
print(sol.combinationSum3(4, 1))