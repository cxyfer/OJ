# @algorithm @lc id=1700 lang=python3 
# @title minimum-time-to-make-rope-colorful


from en.Python3.mod.preImport import *
# @test("abaac",[1,2,3,4,5])=3
# @test("abc",[1,2,3])=0
# @test("aabaa",[1,2,3,4,1])=2
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        i = 0
        while i < n: # 分組循環
            st = i
            mx = s = neededTime[i] # 當前組內的總和, 最大值
            while i < n - 1 and colors[i] == colors[i + 1]: # 同一組
                i += 1
                mx = max(mx, neededTime[i]) # 更新組內最大值
                s += neededTime[i] # 組內總和
            if i > st: 
                ans += (s - mx)
            i += 1
        return ans