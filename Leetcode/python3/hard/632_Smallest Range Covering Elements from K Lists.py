#
# @lc app=leetcode id=632 lang=python3
# @lcpr version=30201
#
# [632] Smallest Range Covering Elements from K Lists
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Greedy + Heap
將問題轉化成從每個list中選一個數，使得這些數的最大值和最小值的差最小
2. Sliding Window
    a. O(d) 枚舉 mn 和 mx 之間的所有值， d = mx - mn = 2e5
    b. O(n log n) 排序 keys ，只枚舉 keys 中的值， n = 3500 * 50 = 175000
"""
# @lc code=start
class Solution1:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = [-inf, inf]
        mx = max([nums[i][0] for i in range(n)])  # initial max value
        hp = [(nums[i][0], i, 0) for i in range(n)]  # (value, row, col)
        heapify(hp)
        while hp:
            mn, i, j = heappop(hp)  # pop min value
            if mx - mn < ans[1] - ans[0]:  # update answer
                ans = [mn, mx]
            if j == len(nums[i]) - 1:
                break
            mx = max(mx, nums[i][j + 1])  # update max value
            heappush(hp, (nums[i][j + 1], i, j + 1))  # push next value
        return ans


class Solution2a:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)  # val -> indices of rows
        for i, arr in enumerate(nums):
            for x in arr:
                pos[x].append(i)

        # 對值域進行滑動窗口
        mx, mn = max(pos), min(pos)
        ans = [mn, mx]
        cnt = [0] * n  # 每個row分別有幾個數字在窗口內
        need = n  # 還有幾個row沒有被涵蓋
        l = mn  # 窗口左端點，注意 mn 可能 < 0，不要初始化成 0
        for r in range(mn, mx + 1):
            if r not in pos:
                continue
            for idx in pos[r]:  # 入窗口
                cnt[idx] += 1
                if cnt[idx] == 1:
                    need -= 1

            while need == 0:  # 滿足條件，縮小窗口
                if r - l < ans[1] - ans[0]:  # 更新答案
                    ans = [l, r]
                if l in pos:
                    for idx in pos[l]:  # 出窗口
                        cnt[idx] -= 1
                        if cnt[idx] == 0:
                            need += 1
                l += 1
        return ans


class Solution2b:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)  # val -> indices of rows
        mn, mx = float("inf"), -float("inf")
        for i, arr in enumerate(nums):
            for x in arr:
                pos[x].append(i)

        mx, mn = max(pos), min(pos)
        ans = [mn, mx]
        cnt = [0] * n  # 每個row分別有幾個數字在窗口內
        need = n  # 還有幾個row沒有被涵蓋

        # 改成對 keys 進行滑動窗口
        keys = sorted(pos.keys())
        l = 0
        for r, x in enumerate(keys):
            for idx in pos[x]:  # 入窗口
                cnt[idx] += 1
                if cnt[idx] == 1:
                    need -= 1

            while need == 0:  # 滿足條件，縮小窗口
                y = keys[l]
                if x - y < ans[1] - ans[0]:  # 更新答案
                    ans = [y, x]
                for idx in pos[y]:  # 出窗口
                    cnt[idx] -= 1
                    if cnt[idx] == 0:
                        need += 1
                l += 1
        return ans


Solution = Solution1
# Solution = Solution2a
# Solution = Solution2b
# @lc code=end

sol = Solution()
print(sol.smallestRange([[-5,-4,-3,-2,-1],[1,2,3,4,5]]))  # [-1, 1]
 

#
# @lcpr case=start
# [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[1,2,3],[1,2,3]]\n
# @lcpr case=end

#

