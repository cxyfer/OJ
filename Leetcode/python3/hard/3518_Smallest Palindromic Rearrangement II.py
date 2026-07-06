#
# @lc app=leetcode id=3518 lang=python3
#
# [3518] Smallest Palindromic Rearrangement II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
試填法 + 組合數學

用試填法，並計算當嘗試在第 i 位填寫 ch 時，後續部分有多少種排列方式 perm，
若 perm < k，則說明第 i 位需要填 ch，否則代表方案數不足，需要填後續的其他字元。

那如何計算 perm 呢？
從組合數學可以得知，若總共有 m 個字元，且每個字元的數量分別為 a1, a2, ..., an，則排列方式總數為：
    perm = m! / (a1! * a2! * ... * an!)

1. 方法一：BigInt
但 m 最大可以到 5000，若每次都重新計算 perm 需要很多次 BigInt 的乘除法，會導致 TLE。
注意到每次試填後會變化的只有 m => m - 1，且某個字元的數量 a_i => a_i - 1，因此可以透過僅計算這兩項的變化來更新 perm 。
需要注意的是：
- 在更新分子的 m! 時，不能直接除以 m!，這是因為分子的 m! 可能已經被分母的某個 a_i! 消掉了，若直接除以 m! 會導致計算錯誤。直接計算 m 的變化即可。
- 類似地，也需要在更新分母的 cnt[ch]! 時，把整除的部分放在最後

2. 方法二：組合數的計算技巧
上述方法需要用到 BigInt，那有沒有辦法不用 BigInt 呢？
注意到 k <= 1e6，可以考慮在計算過程中逐步檢查 perm 會不會超過 k，若超過就直接回傳 perm > k，而不需要計算完整的 perm。

上述的排列數可以改成選取從 m 個字元中選取 a1 個字元、再從剩下的 m - a1 個字元中選取 a2 個字元、...。
也就是組合數的乘積：
    perm = C(m, a1) * C(m - a1, a2) * ... * C(m - a1 - a2 - ... - a(n-1), an)
而對於 C(n, i) = n! / (i! * (n - i)!)，可以改寫成：
    C(n, i) = n * (n - 1) * ... * (n - i + 1) / (i * (i - 1) * ... * 1)
    C(n, i) = n / 1 * (n - 1) / 2 * ... * (n - i + 1) / i
這些分數的前綴乘積一定是整數，因此在前一項上乘以 (n - i + 1) / i 就可以得到下一項，
過程中若 perm > k 就可以直接回傳。
> 可以用每 i 個數一定會有至少一個是 i 的倍數來理解為什麼前綴乘積一定是整數。
"""
# @lc code=start
initialized = False
MAX_N = (int(1e4) + 5) // 2
fact = [1] * MAX_N


# 直接用 BigInt 計算效率很低，但還是勉強能通過
def init():
    global initialized
    for i in range(2, MAX_N):
        fact[i] = fact[i - 1] * i
    initialized = True


class Solution1:
    def smallestPalindrome(self, s: str, k: int) -> str:
        if not initialized:
            init()

        n = len(s)
        # 因為題目確保給定的 s 也是回文，所以只需要統計前半段的字元數量即可
        cnt = Counter(s[: n // 2])
        mid = s[n // 2] if n & 1 else ""

        m = n // 2

        perm = fact[m]
        for val in cnt.values():
            perm //= fact[val]

        if perm < k:
            return ""

        def update(ch: str, delta: int):
            nonlocal perm, m
            # 更新分母的 cnt[ch]!
            perm *= fact[cnt[ch]]
            cnt[ch] += delta
            # 更新分子的 m!
            # 注意在更新分子的 m 時，不能直接除以 m!
            # 這是因為分子的 m! 可能已經被分母的某個 a_i! 消掉了，若直接除以 m! 會導致計算錯誤。
            if delta == 1:
                m += 1
                perm *= m
            else:
                perm //= m
                m -= 1
            # 類似地，也需要在更新分母的 cnt[ch]! 時，把整除的部分放在最後
            perm //= fact[cnt[ch]]

        ans = []
        for _ in range(m):
            for ch in ascii_lowercase:
                if cnt[ch] == 0:
                    continue
                update(ch, -1)
                if k <= perm:
                    ans.append(ch)
                    break
                k -= perm
                update(ch, 1)

        ans = "".join(ans)
        return ans + mid + ans[::-1]


class Solution2:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        # 因為題目確保給定的 s 也是回文，所以只需要統計前半段的字元數量即可
        cnt = Counter(s[: n // 2])
        mid = s[n // 2] if n & 1 else ""

        m = n // 2

        def perm(n: int) -> int:
            # C(n, c1) * C(n - c1, c2) * ... * C(n - c1 - c2 - ... - c(n-1), cn)
            res = 1
            for c in cnt.values():
                if c == 0:
                    continue
                # 用避免溢出的方式逐步計算 C(n, c)
                m = min(c, n - c)  # C(n, m) = C(n, n - m)
                for i in range(1, m + 1):
                    res = res * (n + 1 - i) // i
                    if res >= k:  # 若 res >= k，則直接回傳 k，避免溢出
                        return k
                n -= c
            return res

        if perm(m) < k:
            return ""

        ans = []
        for i in range(m):
            for ch in ascii_lowercase:
                if cnt[ch] == 0:
                    continue
                cnt[ch] -= 1
                p = perm(m - i - 1)
                if k <= p:
                    ans.append(ch)
                    break
                k -= p
                cnt[ch] += 1

        ans = "".join(ans)
        return ans + mid + ans[::-1]


# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.smallestPalindrome("abba", 2))  # baab
print(sol.smallestPalindrome("a", 1))  # a
print(sol.smallestPalindrome("xxnfnxx", 3))  # xxnfnxx
print(sol.smallestPalindrome("aaaabbbbbbaaaa", 34))  # bbabaaaaaababb