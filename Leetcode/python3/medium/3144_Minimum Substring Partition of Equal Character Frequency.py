#
# @lc app=leetcode id=3144 lang=python3
# @lcpr version=30201
#
# [3144] Minimum Substring Partition of Equal Character Frequency
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        劃分型 DP，預處理出以 i 開頭的平衡點 j
        賽時處理是否為平衡點的方法比較粗糙，達到了 O(26 n^2)，用 Python 吃了 TLE (但是 C++ 能過)
        這裡是用 O(1) 的方式更新 mx 和判斷是否為平衡點，所以是 O(n^2)
        - 由於會變大的數只有一個，所以更新 mx 時只要檢查 s[j] 的次數即可
        - 如果是平衡點，則字母數 len(cnt) 乘上最大次數 mx 等於子串長度 j - i + 1

        Reference:
        - https://leetcode.cn/circle/discuss/tb4PG6/
    """
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i): # 從 i 開始劃分
            if i == n:
                return 0
            cnt = Counter()
            mx = 0
            res = float("inf")
            for j in range(i, n): # 枚舉終點 j
                cnt[s[j]] += 1
                # 1. 賽時的寫法，會達到 O(26 n^2)，用 Python 會 TLE
                # mx = max(cnt.values())
                # if all(cnt[k] == mx for k in cnt):
                # 2. 修改後的寫法，只有O(n^2)
                # mx = max(mx, cnt[s[j]]) # 由於變大數只有一個，所以只要檢查 s[j] 的次數即可
                # if j - i + 1 == mx * len(cnt): # 如果是平衡點
                # 3. 靈神的寫法
                if (j - i + 1) % len(cnt): continue # 優化，一定不是平衡點
                c0 = cnt[s[j]]
                if all(cnt[k] == c0 for k in cnt):
                    res = min(res, 1 + dfs(j + 1))
            return res
        return dfs(0)
# @lc code=end

sol = Solution()
print(sol.minimumSubstringsInPartition("aabb")) # 1
print(sol.minimumSubstringsInPartition("fabccddg")) # 3
print(sol.minimumSubstringsInPartition("abababaccddb")) # 2

#
# @lcpr case=start
# "fabccddg"\n
# @lcpr case=end

# @lcpr case=start
# "abababaccddb"\n
# @lcpr case=end

#

