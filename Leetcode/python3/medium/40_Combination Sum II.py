#
# @lc app=leetcode id=40 lang=python3
# @lcpr version=30204
#
# [40] Combination Sum II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
回溯 (Backtracking)
1. 選或不選
2. 枚舉選哪個
"""
class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, s: int):
            if s == target:
                ans.append(path[:])
                return
            if i == n:
                return
            
            x = candidates[i]
            if s + x > target:  # 剪枝
                return
            # 選
            path.append(x)
            dfs(i + 1, s + x)
            path.pop()
            # 不選
            while i < n and candidates[i] == x:
                i += 1
            dfs(i, s)
        dfs(0, 0)
        return ans

class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, s: int):
            if s == target:
                ans.append(path[:])
                return
            for j in range(i, n):  # 考慮下一個選的元素
                """
                若當前元素和 [i, n) 範圍內的上一個元素相同，則不需要再考慮
                這是因為沒選第一個，則也不能選第二個相同的元素，否則會重複計算
                也就是說，若有多個相同的元素，則只能從第一個開始選
                """
                if j > i and candidates[j] == candidates[j - 1]:  # 跳過重複的元素
                    continue
                if s + candidates[j] > target:  # 剪枝
                    break
                path.append(candidates[j])
                dfs(j + 1, s + candidates[j])
                path.pop()
        dfs(0, 0)
        return ans

class Solution(Solution2):
    pass
# @lc code=end


sol = Solution()
print(sol.combinationSum2([2, 5, 2, 1, 2], 5))  # [[1, 2, 2], [5]]


#
# @lcpr case=start
# [10,1,2,7,6,1,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2,5,2,1,2]\n5\n
# @lcpr case=end

#
