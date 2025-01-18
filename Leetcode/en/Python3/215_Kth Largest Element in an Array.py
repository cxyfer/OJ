# @algorithm @lc id=215 lang=python3 
# @title kth-largest-element-in-an-array


from en.Python3.mod.preImport import *
# @test([3,2,1,5,6,4],2)=5
# @test([3,2,3,1,2,4,5,5,6],4)=4
class Solution:
    """
        heapq實現的是min heap，所以要找第k大的元素，就要維護一個size為k的min heap
        Time: O(n + klogn)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for num in nums:
            heapq.heappush(hp, num)
            if len(hp) > k:
                heapq.heappop(hp)
        return hp[0] # hp[0] is the smallest element in the heap