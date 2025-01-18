# @algorithm @lc id=1138 lang=python3 
# @title grumpy-bookstore-owner


from en.Python3.mod.preImport import *
# @test([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3)=16
# @test([1],[0],1)=1
class Solution:
    """
        Prefix Sum
    """
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        pre = [0] * (n+1)
        for i in range(n):
            pre[i+1] = pre[i] + customers[i] * (1 & grumpy[i])
        s = sum(customers[i] for i in range(n) if not grumpy[i])
        ans = 0
        for i in range(n - minutes + 1):
            ans = max(ans, pre[i+minutes] - pre[i])
        return s + ans