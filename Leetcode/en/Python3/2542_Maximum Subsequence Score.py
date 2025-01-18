# @algorithm @lc id=2636 lang=python3 
# @title maximum-subsequence-score


from en.Python3.mod.preImport import *
# @test([1,3,3,2],[2,1,3,4],3)=12
# @test([4,2,3,1,1],[7,5,10,9,6],1)=30
class Solution:
    """
        Min Heap
        - 對 nums2 由大到小排序，確保每取k個數字時，其中最小的數字是最後一個數
        - 因此初始化答案為 nums2[:k] 的和乘上 nums2[k-1] (最小的數字)
        - 接著考慮每次更新的n1, n2，
            - 若 n1 <= heap.top (即目前所選數中的最小值)，因為 n2 是 遞減的，故不會影響答案
            - 若 n1 > heap.top，則更新 heap，並更新答案
    """
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        hp = [num for num, _ in nums[:k]]
        heapq.heapify(hp)
        cur = sum(hp)
        ans = cur * nums[k-1][1] # nums[k-1][1] is the smallest number in nums2[:k]
        for n1, n2 in nums[k:]:
            if n1 > hp[0]:
                cur += n1
                cur -= heapq.heapreplace(hp, n1)
                ans = max(ans, cur * n2)
        return ans