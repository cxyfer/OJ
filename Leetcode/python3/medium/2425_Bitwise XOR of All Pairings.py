#
# @lc app=leetcode id=2425 lang=python3
# @lcpr version=30204
#
# [2425] Bitwise XOR of All Pairings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        def count(nums: List[int]) -> List[int]:
            cnt = [0] * 32
            for x in nums:
                for i in range(32):
                    if x & (1 << i):
                        cnt[i] += 1
            return cnt
        cnt1, cnt2 = count(nums1), count(nums2)
        ans = 0
        for i in range(32):
            cur = (cnt1[i] * (m - cnt2[i])) + ((n - cnt1[i]) * cnt2[i])
            ans += ((cur & 1) << i)
        return ans
    
class Solution2:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        ans = 0
        if m & 1:
            ans ^= reduce(xor, nums1)
        if n & 1:
            ans ^= reduce(xor, nums2)
        return ans

class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.xorAllNums([2,1,3], [10,2,5,0]))
#
# @lcpr case=start
# [2,1,3]\n[10,2,5,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

