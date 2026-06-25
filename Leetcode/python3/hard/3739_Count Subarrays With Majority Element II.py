#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
"""
子陣列 [l, r] 滿足條件，等同於 cnt_target - cnt_other > 0，
這個值可以透過前綴和來維護，當 s[r] - s[l - 1] > 0 時，子陣列 [l, r] 滿足題意。
O(n^2) 的解法是枚舉所有子陣列，可以通過 I 。

進一步優化，我們能不能在枚舉右端點 r，維護有多少個滿足 l < r 且 s[l - 1] < s[r] 的左端點？
自此可以轉換成二維偏序問題，類似求逆序對，可以使用 BIT 來維護。
注意上述前綴和的值域是 [-n, n]，需要將其做偏移，映射到 [1, 2n + 1]。

Hint1: ||子陣列 [l, r] 滿足條件，等同於 cnt_target - cnt_other > 0，即 target 貢獻 +1，其他元素貢獻 -1，因此可以寫成前綴和的形式||
Hint2: ||寫成前綴和後，對於右端點 r，我們能不能維護有多少個滿足 l < r 且 s[l - 1] < s[r] 的左端點？||
Hint3: ||這個問題是二維偏序問題，此類問題的經典是求逆序對，可以使用 BIT 來維護、或是在 Merge Sort 的過程中維護||
"""


# @lc code=start
class BIT:  # PURQ, 1-based
    __slots__ = ["tree"]

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:  # 求 nums[:k+1] 之和
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= k & -k
        return res

    def query(self, l: int, r: int) -> int:  # 求 nums[l:r+1] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)


class Solution1:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        ans = 0
        s = n + 1  # offset 為 n + 1，起始為 0 + offset = n + 1
        bit = BIT(2 * n + 1)  # [-n, n] -> [1, 2n + 1]
        bit.add(s, 1)
        for x in nums:
            s += 1 if x == target else -1
            ans += bit.query(1, s - 1)
            bit.add(s, 1)
        return ans


class Solution2:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = s = 0
        sl = SortedList()
        sl.add(0)
        for x in nums:
            s += 1 if x == target else -1
            ans += sl.bisect_left(s)
            sl.add(s)
        return ans


class Solution3:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cnt = [0] * (2 * n + 1)  # [-n, n] => [0, 2n]

        # s = cnt_target - cnt_other
        s = n  # offset 為 n，起始為 0 + offset = n
        cnt[s] = 1
        # lt = 有多少個 l 滿足 l < r 且 s[l - 1] < s[r]
        ans = lt = 0
        for x in nums:
            if x == target:
                lt += cnt[s]
                s += 1
            else:
                lt -= cnt[s - 1]
                s -= 1
            ans += lt
            cnt[s] += 1
        return ans


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end
sol = Solution()
print(sol.countMajoritySubarrays([1,2,2,3], 2))  # 5
print(sol.countMajoritySubarrays([1,1,1,1], 1))  # 10
print(sol.countMajoritySubarrays([1,2,3], 4))  # 0