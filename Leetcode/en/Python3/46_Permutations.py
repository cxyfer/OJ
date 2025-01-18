# @algorithm @lc id=46 lang=python3 
# @title permutations


from en.Python3.mod.preImport import *
# @test([1,2,3])=[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# @test([0,1])=[[0,1],[1,0]]
# @test([1])=[[1]]
class Solution:
    """
        1. 用一個 set 紀錄還沒被選過的數字
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return self.solve1(nums)
        return self.solve2(nums)
    def solve1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        res = [0] * n
        def dfs(cur: int, avail: set):
            if cur == n:
                ans.append(res.copy())
                return
            for x in avail:
                res[cur] = x
                dfs(cur+1, avail-{x})
        dfs(0, set(nums))
        return ans
    """
        2. 交換法
    """
    def solve2(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def perm(nums, i, n):
            if i == n:
                ans.append(nums.copy())
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                perm(nums, i+1, n)
                nums[i], nums[j] = nums[j], nums[i]
        perm(nums, 0, len(nums))
        return ans
        