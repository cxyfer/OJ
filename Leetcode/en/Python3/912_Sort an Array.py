# @algorithm @lc id=948 lang=python3 
# @title sort-an-array


from en.Python3.mod.preImport import *
# @test([5,2,3,1])=[1,2,3,5]
# @test([5,1,1,2,0,0])=[0,0,1,1,2,5]
class Solution:
    """
        Heap sort
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hp = [-val for val in nums]
        heapq.heapify(hp) # O(n)
        ans = [-1] * n
        last = n - 1
        while hp:
            ans[last] = -heapq.heappop(hp)
            last -= 1
        return ans
        
