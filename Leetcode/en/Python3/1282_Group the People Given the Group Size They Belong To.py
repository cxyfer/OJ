# @algorithm @lc id=1407 lang=python3 
# @title group-the-people-given-the-group-size-they-belong-to


from en.Python3.mod.preImport import *
# @test([3,3,3,3,3,1,3])=[[5],[0,1,2],[3,4,6]]
# @test([2,1,3,3,3,2])=[[1],[0,5],[2,3,4]]
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash_map = defaultdict(list)
        ans = []
        for i, size in enumerate(groupSizes):
            hash_map[size].append(i)
            if len(hash_map[size]) == size:
                ans.append(hash_map.pop(size))
        return ans