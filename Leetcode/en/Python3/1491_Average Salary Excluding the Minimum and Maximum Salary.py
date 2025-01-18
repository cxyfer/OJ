# @algorithm @lc id=1584 lang=python3 
# @title average-salary-excluding-the-minimum-and-maximum-salary


from en.Python3.mod.preImport import *
# @test([4000,3000,1000,2000])=2500.00000
# @test([1000,2000,3000])=2000.00000
class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        ans = 0
        mx, mn = float('-inf'), float('inf')
        for num in salary:
            mx = max(mx, num)
            mn = min(mn, num)
            ans += num
        return (ans-mx-mn)/(n-2)