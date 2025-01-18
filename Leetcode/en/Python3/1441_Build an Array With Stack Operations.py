# @algorithm @lc id=1552 lang=python3 
# @title build-an-array-with-stack-operations


from en.Python3.mod.preImport import *
# @test([1,3],3)=["Push","Push","Pop","Push"]
# @test([1,2,3],3)=["Push","Push","Push"]
# @test([1,2],4)=["Push","Push"]
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        m = len(target)
        ans = []
        i, j = 1, 0 # i is the current number, j is the index of target
        while i <= n and j < m:
            if target[j] == i: # 要這個數字
                ans.append("Push")
                j += 1
            else: # 不要這個數字
                ans.append("Push")
                ans.append("Pop")
            i += 1
        return ans