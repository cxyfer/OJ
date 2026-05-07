#
# @lc app=leetcode id=3660 lang=python3
#
# [3660] Jump Game IX
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

class Solution1:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        fa = list(range(n))
        sz = [1] * n
        mx = nums[:]
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x: int, y: int) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            if sz[fx] < sz[fy]:
                fx, fy = fy, fx
            fa[fy] = fx
            sz[fx] += sz[fy]
            mx[fx] = max(mx[fx], mx[fy])
            return True

        sl = SortedList(key=lambda x: nums[x])
        for i in range(n):
            idx = sl.bisect_right(i)
            if idx < len(sl):
                union(i, sl[idx])
                # union(i, sl[-1])
            sl.add(i)

        sl.clear()
        for i in range(n - 1, -1, -1):
            idx = sl.bisect_left(i) - 1
            if idx >= 0:
                union(i, sl[0])
                # union(i, sl[idx])
            sl.add(i)

        return [mx[find(u)] for u in range(n)]

class Solution2:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        fa = list(range(n))
        sz = [1] * n
        mx = nums[:]
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x: int, y: int) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            if sz[fx] < sz[fy]:
                fx, fy = fy, fx
            fa[fy] = fx
            sz[fx] += sz[fy]
            mx[fx] = max(mx[fx], mx[fy])
            return True

        st = []
        for i, x in enumerate(nums):
            while st and mx[fa[st[-1]]] > x:
                union(i, st.pop())
            st.append(i)

        return [mx[find(u)] for u in range(n)]

class Solution3:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        pre = list(accumulate(nums, max))  # 前綴最大值
        suf = float('inf') # 後綴最小值
        for i in range(n - 1, -1, -1):
            ans[i] = pre[i] if pre[i] <= suf else ans[i + 1]
            suf = min(suf, nums[i])
        return ans

# Solution = Solution1
Solution = Solution2
# Solution = Solution3
# @lc code=end
sol = Solution()
print(sol.maxValue([2,1,3]))  # [2,2,3]
print(sol.maxValue([2,3,1]))  # [3,3,3]
print(sol.maxValue([19,25,12,21]))  # [25,25,25,25]
print(sol.maxValue([30,21,5,35,24]))  # [35, 35, 35, 35, 35]
print(sol.maxValue([20,21,25,15]))  # [25, 25, 25, 25]
print(sol.maxValue([6,7,1,8,9,2]))  # [9, 9, 9, 9, 9, 9]

# from tqdm import tqdm

# for kase in tqdm(range(100000)):
#     n = randint(10, 100)
#     nums = [randint(1, n) for _ in range(n)]
#     if Solution1().maxValue(nums) != Solution2().maxValue(nums):
#         print(f"\nCase {kase} failed")
#         print(nums)
#         print("Solution1:")
#         print(Solution1().maxValue(nums))
#         print("Solution2:")
#         print(Solution2().maxValue(nums))
#         break