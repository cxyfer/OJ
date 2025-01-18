# @algorithm @lc id=216 lang=python3 
# @title combination-sum-iii


from en.Python3.mod.preImport import *
# @test(3,7)=[[1,2,4]]
# @test(3,9)=[[1,2,6],[1,3,5],[2,3,4]]
# @test(4,1)=[]
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