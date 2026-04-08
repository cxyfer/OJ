#
# @lc app=leetcode id=3892 lang=python3
#
# [3892] Minimum Operations to Achieve At Least K Peaks
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
1. 多了一個維度的打家劫舍DP
2. 反悔貪心
3. WQS二分 (Aliens Trick)  *待補
"""
class Solution1:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if k > n // 2:
            return -1

        A = [max(max(nums[(i - 1) % n], nums[(i + 1) % n]) + 1 - nums[i], 0) for i in range(n)]

        def f(arr: list[int], k: int) -> int:
            n = len(arr)
            @cache
            def dfs(i: int, j: int) -> int:
                if j == 0:
                    return 0
                # if i >= n:  # MLE
                if i >= n or j > (n - i + 1) // 2:
                    return float('inf')
                return min(arr[i] + dfs(i + 2, j - 1), dfs(i + 1, j))
            ans = dfs(0, k)
            dfs.cache_clear()
            return ans
        # 分別計算不選擇第一個元素和最後一個元素的情況，兩者取最小值
        return min(f(A[1:], k), f(A[:-1], k))

class Solution2:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if k > n // 2:
            return -1

        A = [max(max(nums[(i - 1) % n], nums[(i + 1) % n]) + 1 - nums[i], 0) for i in range(n)]

        def f(nums: list[int], k: int) -> list[int]:
            """
            反悔貪心
            當選擇位置為 x 的元素時，則不能選擇兩側的 L(x) 和 R(x)，
            如果要放棄原本選擇的 x，改成選擇 L(x) 或 R(x)，則反悔的代價為 val(L(x)) + val(R(x)) - val(x)。
            故可以每次選擇最小代價的元素，將其加入答案中，並將其與相鄰的元素合併。
            可以用 Doubly Linked List + Min Heap 來維護這個過程。

            然而每次取出一個元素時，他必然是局部最小值，因此也能直接用 Stack 來維護這個過程。
            """
            INF = 10**30
            nums = [INF] + nums + [INF]  # 左右邊界哨兵

            res = []  # 收集所有「被選中的 p 值」
            st = []
            pp = p = None
            for v in nums:
                while pp is not None and p is not None and pp >= p <= v:  # p 是局部最小值
                    res.append(p)  # 選擇 p
                    v += pp - p  # 合併兩側元素 v = pp + v - p，作為反悔代價
                    p = st.pop() if st else None
                    pp = st.pop() if st else None
                if pp is not None:
                    st.append(pp)
                pp, p = p, v
            # 期望 O(n): 只把前 k 小放到前 k 個位置，不做完整排序
            self.nth_element(res, k)
            return sum(res[:k])
        # 分別計算不選擇第一個元素和最後一個元素的情況，兩者取最小值
        return min(f(A[1:], k), f(A[:-1], k))

    def nth_element(self, nums: list[int], k: int) -> None:
        """
        Selection Algorithm (Quickselect, 3-way partition).
        Reorder `nums` in-place so that the first `k` positions contain
        exactly `k` smallest elements (order inside first k is unspecified).
        `k` is a count, not index. Expected O(n) time.
        """
        n = len(nums)
        target = k - 1  # 0-index of the k-th smallest element
        l, r = 0, n - 1
        while l <= r:
            pivot = nums[randint(l, r)]

            # 3-way partition: [l, lt) < pivot, [lt, i) == pivot, [gt+1, r] > pivot
            lt, i, gt = l, l, r
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            if target < lt:
                r = lt - 1
            elif target > gt:
                l = gt + 1
            else:
                return

class Solution3:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if k > n // 2:
            return -1

        A = [max(max(nums[(i - 1) % n], nums[(i + 1) % n]) + 1 - nums[i], 0) for i in range(n)]

        def f(nums: list[int], k: int) -> int:
            """使用 WQS Binary Search (Aliens Trick) 計算最少操作次數"""

            def check(c: int):
                """檢查當 f_c(S) = cost(S) + c * |S| 時的最小成本，其中 S 為選擇的元素集合"""
                # 維護 (cost, cnt)，為滿足單調性，在 cost 相同時選擇 cnt 較小的
                f0, f1 = (0, 0), (float('inf'), 0)  # 不選/選 當前元素
                for x in nums:
                    f0, f1 = min(f0, f1), (f0[0] + x + c, f0[1] + 1)
                return min(f0, f1)

            # 極端情況下從選 k - 1 個增加到 k 個需要 k * mx 的成本 
            mx = max(nums)
            left, right = -mx * k, mx * k
            while left <= right:
                mid = (left + right) // 2
                _, cnt = check(mid)
                if cnt <= k:  # 要多選，成本需要降低
                    right = mid - 1
                else:  # 要少選，成本需要升高
                    left = mid + 1
            return check(left)[0] - k * left

        # 分別計算不選擇第一個元素和最後一個元素的情況，兩者取最小值
        return min(f(A[1:], k), f(A[:-1], k))

# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.minOperations([2,1,2], 1)) # 1
print(sol.minOperations([4,5,3,6], 2)) # 0
print(sol.minOperations([3,7,3], 2)) # -1
print(sol.minOperations([-14,-2,-14], 0)) # 0
print(sol.minOperations([-3,-8,8,5], 1)) # 0