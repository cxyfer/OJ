# @algorithm @lc id=1458 lang=python3 
# @title sort-integers-by-the-number-of-1-bits


from en.Python3.mod.preImport import *
# @test([0,1,2,3,4,5,6,7,8])=[0,1,2,4,8,3,5,6,7]
# @test([1024,512,256,128,64,32,16,8,4,2,1])=[1,2,4,8,16,32,64,128,256,512,1024]
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i in arr:
            dic[bin(i).count('1')].append(i)
        return [x for key in sorted(dic.keys()) for x in sorted(dic[key])]
        