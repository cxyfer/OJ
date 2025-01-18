# @algorithm @lc id=1552 lang=python3 
# @title build-an-array-with-stack-operations


from en.Python3.mod.preImport import *
# @test([1,3],3)=["Push","Push","Pop","Push"]
# @test([1,2,3],3)=["Push","Push","Push"]
# @test([1,2],4)=["Push","Push"]
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        idx = 0
        for i in range(1, n+1):
            if idx == len(target):
                break
            if i == target[idx]:
                ans.append("Push")
                idx += 1
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans