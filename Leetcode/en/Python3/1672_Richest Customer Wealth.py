# @algorithm @lc id=1791 lang=python3 
# @title richest-customer-wealth


from en.Python3.mod.preImport import *
# @test([[1,2,3],[3,2,1]])=6
# @test([[1,5],[7,3],[3,5]])=10
# @test([[2,8,7],[7,1,3],[1,9,5]])=17
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])