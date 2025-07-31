#
# @lc app=leetcode id=1521 lang=python3
# @lcpr version=30203
#
# [1521] Find a Value of a Mysterious Function Closest to Target
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Similar to 3171. Find Subarray With Bitwise OR Closest to K
把 OR 換成 AND 即是本題
"""
# @lc code=start
class Solution1a:
    def closestToTarget(self, nums: List[int], k: int) -> int:
        st = set()
        ans = float('inf')
        for x in nums: # 枚舉右端點
            # 保存以 x 為右端點的所有 AND 結果
            st = {y & x for y in st}
            st.add(x)
            ans = min(ans, min(abs(y - k) for y in st))
        return ans

class Solution1b:
    def closestToTarget(self, nums: List[int], k: int) -> int:
        st = []
        ans = float('inf')
        for x in nums: # 枚舉右端點
            # 保存以 x 為右端點的所有 AND 結果，注意由於 AND 的性質，這裡的 st2 是遞減的
            st2 = [x]
            for y in st:
                # 保持有序性質以便去重，省去一個 set
                if y & x != st2[-1]:
                    st2.append(y & x)
            # 更新答案
            for y in st2:
                ans = min(ans, abs(y - k))
            st = st2
        return ans

class Solution1c:
    def closestToTarget(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        # 枚舉右端點 i，在枚舉 i 時將 nums[j] 原地修改成 AND(nums[j...i])
        # 此時有 A_j ⊇ A_{j+1} ⊇ A_{j+2} ⊇ ... ⊇ A_i 的性質，即 A_{j+1} 是 A_j 的子集，以此類推
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            for j in range(i - 1, -1, -1):
                # 如果 x 是 nums[j] 的子集，則 x 也會是 nums[j-1] 的子集，以此類推，故不用更新
                if nums[j] & x == nums[j]:
                    break
                nums[j] &= x
                ans = min(ans, abs(nums[j] - k))
        return ans

class Solution2:
    def closestToTarget(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        left = cur = 0
        cnt = [0] * 32
        for right, x in enumerate(nums):
            for b in range(32):
                if x & (1 << b):
                    cnt[b] += 1
                    if cnt[b] == (right - left + 1):
                        cur |= 1 << b
                else:
                    cur &= ~(1 << b)
            ans = min(ans, abs(cur - k))
            while left < right and cur <= k:
                for b in range(32):
                    if nums[left] & (1 << b):
                        cnt[b] -= 1
                    else:
                        if cnt[b] == (right - (left + 1) + 1):
                            cur |= 1 << b
                left += 1
                ans = min(ans, abs(cur - k))
        return ans
    
class Solution3a:
    def closestToTarget(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        # Stack 由上到下保存 AND(nums[i...bottom]), AND(nums[i+1...bottom]) 等結果
        st = [-1]  # 加入哨兵，避免 st 為空
        left, right_and = 0, -1
        for right, x in enumerate(nums):
            right_and &= x
            while left <= right and st[-1] & right_and <= k:
                ans = min(ans, k - (st.pop() & right_and))
                left += 1
                # 重新構建 Stack
                if not st:
                    st.append(-1)  # 哨兵
                    for i in range(right, left - 1, -1):
                        st.append(st[-1] & nums[i])
                    right_and = -1
            if left <= right:
                ans = min(ans, (st[-1] & right_and) - k)
        return ans
    
class Solution3b:
    def closestToTarget(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        # 原地使用 nums 作為 Stack，由上到下保存 AND(nums[i...bottom]), AND(nums[i+1...bottom]) 之結果
        left = bottom = 0
        right_and = -1
        for right, x in enumerate(nums):
            right_and &= x
            while left <= right and nums[left] & right_and <= k:
                ans = min(ans, k - (nums[left] & right_and))
                left += 1
                # 重新構建 Stack
                if bottom < left:
                    for i in range(right - 1, left - 1, -1):
                        nums[i] &= nums[i + 1]
                    bottom = right
                    right_and = -1
            if left <= right:
                ans = min(ans, (nums[left] & right_and) - k)
        return ans

# Solution = Solution1a
# Solution = Solution1b
# Solution = Solution1c
# Solution = Solution2
Solution = Solution3a
# Solution = Solution3b
# @lc code=end

sol = Solution()
print(sol.closestToTarget([9,12,3,7,15], 5))  # 2
print(sol.closestToTarget([1000000,1000000,1000000], 1))  # 999999
print(sol.closestToTarget([1,2,4,8,16], 0))  # 0

#
# @lcpr case=start
# [9,12,3,7,15]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1000000,1000000,1000000]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,8,16]\n0\n
# @lcpr case=end

#

