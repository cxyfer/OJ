# @algorithm @lc id=890 lang=python3 
# @title lemonade-change


from en.Python3.mod.preImport import *
# @test([5,5,5,10,20])=true
# @test([5,5,10,10,20])=false
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt_5 = cnt_10 = cnt_20 = 0
        for x in bills:
            if x == 5:
                cnt_5 += 1
            elif x == 10:
                cnt_10 += 1
                cnt_5 -= 1
            else:
                cnt_20 += 1
                if cnt_10 > 0:
                    cnt_10 -= 1
                    cnt_5 -= 1
                else:
                    cnt_5 -= 3
            if cnt_5 < 0:
                return False
        return True