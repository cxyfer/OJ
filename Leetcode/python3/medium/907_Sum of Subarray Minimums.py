#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9) + 7


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        # L[i] 表示左側第一個 <= arr[i] 的位置
        # R[i] 表示右側第一個 < arr[i] 的最小位置
        L = [-1] * n
        R = [n] * n
        st = []
        for i, x in enumerate(arr):
            while st and x < arr[st[-1]]:
                R[st.pop()] = i
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            x = arr[i]
            while st and x <= arr[st[-1]]:
                L[st.pop()] = i
            st.append(i)

        ans = 0
        for i, x in enumerate(arr):
            ans += x * (i - L[i]) * (R[i] - i) % MOD
            ans %= MOD
        return ans % MOD
# @lc code=end
sol = Solution()
print(sol.sumSubarrayMins([3,1,2,4]))  # 17