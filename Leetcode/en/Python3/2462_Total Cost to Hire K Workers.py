# @algorithm @lc id=2553 lang=python3 
# @title total-cost-to-hire-k-workers


from en.Python3.mod.preImport import *
# @test([17,12,10,2,7,2,11,20,8],3,4)=11
# @test([1,2,4,1],3,3)=4
# @test([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2)=423
# @test([10,1,11,10], 2, 1)=11
class Solution:
    """
        兩個 min heap，要避免重疊!!!
    """
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        # 如果 candidates >= n/2 (會重疊)，則直接取前k個最小的數字
        if candidates * 2 >= n:
            return sum(sorted(costs)[:k])
        # 否則，取前 candidates 個最小的數字，以及後 candidates 個最小的數字
        hp1 = costs[:candidates]
        heapify(hp1)
        hp2 = costs[-candidates:]
        heapify(hp2)
        ans = 0
        left = candidates # 下一個要加入 hp1 的數字的 index
        right = n - 1 - candidates # 下一個要加入 hp2 的數字的 index
        while (k > 0 and left <= right):
            if hp1[0] <= hp2[0]:
                ans += heapreplace(hp1, costs[left])
                left += 1
            else:
                ans += heapreplace(hp2, costs[right])
                right -= 1
            k -= 1
        if k > 0: # 兩個heap重疊了，但還沒取完k個數字
            rem = hp1 + hp2
            rem.sort()
            ans += sum(rem[:k])
        return ans