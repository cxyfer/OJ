# @algorithm @lc id=1798 lang=python3 
# @title max-number-of-k-sum-pairs


from en.Python3.mod.preImport import *
# @test([1,2,3,4],5)=2
# @test([3,1,3,4,3],6)=1
class Solution1:
    """
        1. Hash map
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        ans = 0
        for num in nums:
            if cnt[k - num] > 0:
                cnt[k - num] -= 1
                ans += 1
            else:
                cnt[num] += 1
        return ans

class Solution2:
    """
        2. Simple Hash map
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        for num in cnt:
            if num * 2 < k: # 避免重複計算，num和k-num只取兩者之間較小的
                ans += min(cnt[num], cnt[k - num])
            elif num * 2 == k:
                ans += cnt[num] // 2
        return ans
    
class Solution(Solution2):
    ...