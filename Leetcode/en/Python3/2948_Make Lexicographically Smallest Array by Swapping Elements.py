# @algorithm @lc id=3219 lang=python3 
# @title make-lexicographically-smallest-array-by-swapping-elements


from en.Python3.mod.preImport import *
# @test([1,5,3,9,8],2)=[1,3,5,8,9]
# @test([1,7,6,18,2,1],3)=[1,6,7,18,1,2]
# @test([1,7,28,19,10],3)=[1,7,28,19,10]
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        ans = [0] * n

        lst = [(num, idx) for idx, num in enumerate(nums)]
        lst.sort()

        i = 0
        while i < n:
            num, idx = lst[i]
            hp_idx = []
            hp_num = []
            heappush(hp_idx, idx)
            heappush(hp_num, num)
            j = i + 1
            while j < n and lst[j][0] - lst[j-1][0] <= limit:
                heappush(hp_idx, lst[j][1])
                heappush(hp_num, lst[j][0])
                j += 1
            # print(i, j, lst[i:j])
            # print(hp_idx, hp_num)
            while hp_idx:
                ans[heappop(hp_idx)] = heappop(hp_num)
            i = j
        return ans