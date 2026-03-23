#
# @lc app=leetcode id=3878 lang=python3
#
# [3878] Count Good Subarrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        B = max(nums).bit_length()

        L = [0] * n
        last = [-1] * B
        mp = defaultdict(lambda: -1)
        for i, x in enumerate(nums):
            L[i] = mp[x] + 1
            for b in range(B):
                if (x >> b) & 1:
                    last[b] = i
                else:
                    L[i] = max(L[i], last[b] + 1)
            mp[x] = i

        R = [n - 1] * n
        last = [n] * B
        for i in range(n - 1, -1, -1):
            x = nums[i]
            for b in range(B):
                if (x >> b) & 1:
                    last[b] = i
                else:
                    R[i] = min(R[i], last[b] - 1)

        return sum((i - L[i] + 1) * (R[i] - i + 1) for i in range(n))

class Solution2:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        L = [0] * n
        st = []
        for i, x in enumerate(nums):
            while st and nums[st[-1]] < x and nums[st[-1]] | x == x:
                st.pop()
            L[i] = st[-1] + 1 if st else 0
            st.append(i)

        R = [n - 1] * n
        st = []
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while st and nums[st[-1]] | x == x:
                st.pop()
            R[i] = st[-1] - 1 if st else n - 1
            st.append(i)
        return sum((i - L[i] + 1) * (R[i] - i + 1) for i in range(n))

class Solution3:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        ans = 0
        arr: list[tuple[int, int]] = []  # (or_val, left)
        last = defaultdict(lambda: -1)
        for i, x in enumerate(nums):
            last[x] = i

            # Logtrick
            arr.append((x, i))
            arr2 = []
            for y, left in arr:
                if not arr2 or y | x != arr2[-1][0]:
                    arr2.append((y | x, left))
            arr = arr2

            for j, (y, left) in enumerate(arr):
                # [left, i] ... [right, i] 的 OR 值都是 y
                right = arr[j + 1][1] - 1 if j + 1 < len(arr) else i
                # 由於 OR 的性質，上一個 y 不可能出現在 > right 的位置，因此檢查是否 >= left 即可
                if last[y] >= left:
                    ans += min(right, last[y]) - left + 1
        return ans

# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.countGoodSubarrays([4,2,3]))  # 4
print(sol.countGoodSubarrays([1,3,1]))  # 6