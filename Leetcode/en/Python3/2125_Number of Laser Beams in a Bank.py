# @algorithm @lc id=2244 lang=python3 
# @title number-of-laser-beams-in-a-bank


from en.Python3.mod.preImport import *
# @test(["011001","000000","010100","001000"])=8
# @test(["000","111","000"])=0
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cnt = [line.count('1') for line in bank]
        ans = 0
        pre = 0
        for x in cnt:
            if x > 0:
                ans += pre * x
                pre = x
        return ans