#
# @lc app=leetcode id=4119 lang=python3
#
# [4119] Minimum Set Bits in a Valid Integer
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Biweekly Contest 196 - Q4
1. Sliding Window + SOS DP
2. Sliding Window + Stack + SOS DP

設每個長度為 k 的子陣列之位元 AND 結果為 xi，問題等價於找一個 1 的個數最少的整數 y，
使得對所有 xi 都有 (y & xi) != 0。
取補集 z = (U - 1) ^ y（其中 B = max(nums).bit_length(), U = 1 << B）：
- y 與所有 xi 有交集  <=>  不存在任何 xi 是 z 的子集。
- 最小化 popcount(y)  <=>  最大化滿足條件的 popcount(z)，答案為 B - max(popcount(z))。

利用 SOS DP 維護 f[s] 表示 s 的子集是否包含任意 xi：
若 f[z] == False，則 z 的補集 y 為合法解。

而有兩種方法可以求出所有長度為 k 的子陣列之位元 AND 結果：

1. 滑動窗口（按位統計）: O(n * B)
   維護長度為 k 的滑動窗口內每個位元為 1 的個數 cnt[b]，當 cnt[b] == k 時該位元在 xi 中為 1。

2. 滑動窗口（雙棧模擬隊列）+ SOS DP: O(n)
   因為 AND 沒有逆運算，可將窗口拆成左半部後綴 AND（Stack）與右半部前綴 AND（right_and），
   每 k 步在 Stack 為空時重建一次，以均攤 O(n) 求出所有長度為 k 的子陣列 AND 結果。
   （見 3171. Find Subarray With Bitwise OR Closest to K，AND 的單位元素改為 -1）
"""
# @lc code=start
class Solution1:
    def minSetBits(self, nums: list[int], k: int) -> int:
        B = max(nums).bit_length()
        U = 1 << B
        f = [False] * U
        cnt = [0] * B

        # 滑動窗口求出長度為 k 的子陣列的 AND 結果
        for right, v in enumerate(nums):
            # 1. 入窗口
            for b in range(B):
                if (v >> b) & 1:
                    cnt[b] += 1

            left = right - k + 1
            if left < 0:
                continue

            # 2. 計算 xi = AND(nums[i...i+k-1])
            x = 0
            for b in range(B):
                if cnt[b] == k:
                    x |= 1 << b
            f[x] = True

            # 3. 出窗口
            v = nums[left]
            for b in range(B):
                if (v >> b) & 1:
                    cnt[b] -= 1

        # SOS DP
        # f[s] 表示 s 的子集是否包含任意的 xi
        # 因此 f[s] = False 表示 s' 與 xi 有交集
        for b in range(B):
            s = 0
            while s < U:
                s |= 1 << b  # 優化：直接跳到下一個包含 b 位的數字
                f[s] = f[s] or f[s ^ (1 << b)]
                s += 1

        mx = -inf
        for z in range(U):
            if not f[z]:
                mx = max(mx, z.bit_count())

        return -1 if mx < 0 else B - mx


class Solution2:
    def minSetBits(self, nums: list[int], k: int) -> int:
        B = max(nums).bit_length()
        U = 1 << B
        f = [False] * U

        # Sliding Window + Stack， O(n) 求出長度為 k 的子陣列的 AND 結果
        # 倒序保存左半部後綴 AND，由上到下為 AND(nums[i...bottom]), AND(nums[i+1...bottom]), ... 之結果
        # 見 3171. Find Subarray With Bitwise OR Closest to K 的說明
        st = []
        right_and = -1
        for right, x in enumerate(nums):
            right_and &= x
            if right < k - 1:
                continue
            if not st:
                # 每 k 步重建一次：將 [right - k + 1, right] 倒序壓入 st
                cur = -1
                for i in range(right, right - k, -1):
                    cur &= nums[i]
                    st.append(cur)
                right_and = -1
            f[st[-1] & right_and] = True
            st.pop()

        # SOS DP
        # f[s] 表示 s 的子集是否包含任意的 xi
        # 因此 f[s] = False 表示 s' 與 xi 有交集
        for b in range(B):
            s = 0
            while s < U:
                s |= 1 << b  # 優化：直接跳到下一個包含 b 位的數字
                f[s] = f[s] or f[s ^ (1 << b)]
                s += 1

        mx = -inf
        for z in range(U):
            if not f[z]:
                mx = max(mx, z.bit_count())

        return -1 if mx < 0 else B - mx


# Solution = Solution1
Solution = Solution2
# @lc code=end
sol = Solution()
print(sol.minSetBits([3,5,12], 1))  # 2