# @algorithm @lc id=917 lang=python3 
# @title boats-to-save-people


from en.Python3.mod.preImport import *
# @test([1,2],3)=1
# @test([3,2,2,1],3)=3
# @test([3,5,3,4],5)=4
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit: # 只能帶比較重的那一個人
                j -= 1
            else: # 可以帶兩個人
                i += 1
                j -= 1
            ans += 1
        return ans