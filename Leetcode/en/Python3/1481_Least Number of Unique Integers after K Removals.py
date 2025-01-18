# @algorithm @lc id=1604 lang=python3 
# @title least-number-of-unique-integers-after-k-removals


from en.Python3.mod.preImport import *
# @test([5,5,4],1)=1
# @test([4,3,1,1,3,3,2],3)=2
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr) 
        keys = sorted(cnt.keys(), key=cnt.get)
        i = 0
        while k:
            if k >= cnt[keys[i]]:
                k -= cnt[keys[i]]
                i += 1
            else:
                break
        return len(keys) - i