#
# @lc app=leetcode id=1248 lang=python3
# @lcpr version=30204
#
# [1248] Count Number of Nice Subarrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Prefix Sum + Binary Search
    2. Prefix Sum
    3. Sliding Window + Math
"""
class Solution1:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x % 2
        ans = 0
        for i in range(n):
            ans += bisect_right(s, s[i] + k) - bisect_left(s, s[i] + k)
        return ans

class Solution2:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = s = 0
        cnt = [1] + [0] * n
        for x in nums:
            s += x & 1
            if s >= k:
                ans += cnt[s - k]
            cnt[s] += 1
        return ans
    
class Solution3:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [i for i, x in enumerate(nums) if x & 1]
        ans = 0
        for i in range(len(odd) - k + 1): # 枚舉最左邊的奇數
            j = i + k - 1 # 最右邊的奇數
            lcnt = odd[i] - (odd[i-1] if i > 0 else -1) - 1 # 左邊的偶數個數
            rcnt = (odd[j+1] if j + 1 < len(odd) else n) - odd[j] - 1 # 右邊的偶數個數
            ans += (lcnt + 1) * (rcnt + 1)
        return ans

# class Solution(Solution1):
# class Solution(Solution2):
class Solution(Solution3):
    pass
# @lc code=end

sol = Solution()
print(sol.numberOfSubarrays([1,1,2,1,1], 3)) # 2
print(sol.numberOfSubarrays([2,4,6], 1)) # 0
print(sol.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)) # 16

#
# @lcpr case=start
# [1,1,2,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,1,2,2,1,2,2,2]\n2\n
# @lcpr case=end

#

