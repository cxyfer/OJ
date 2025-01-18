# @algorithm @lc id=3183 lang=python3 
# @title find-the-k-or-of-an-array


from en.Python3.mod.preImport import *
# @test([7,12,9,8,9,15],4)=9
# @test([2,12,1,11,4,5],6)=0
# @test([10,8,5,9,11,6,8],1)=15
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        for num in nums:
            idx = 0
            while num:
                cnt[idx] += num & 1
                num >>= 1
                idx += 1
        ans = 0
        for b in cnt.keys():
            ans += (1 << b) if cnt[b] >= k else 0
        return ans
    
sol = Solution()
print(sol.findKOr([7,12,9,8,9,15], 4)) # 9
print(sol.findKOr([2,12,1,11,4,5], 6)) # 0
print(sol.findKOr([10,8,5,9,11,6,8], 1)) #15