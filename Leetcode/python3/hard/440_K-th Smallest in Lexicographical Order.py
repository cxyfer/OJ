#
# @lc app=leetcode id=440 lang=python3
# @lcpr version=30204
#
# [440] K-th Smallest in Lexicographical Order
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    """
    Similar Problems:
    - 60. Permutation Sequence
    - UVA-941 Permutations
    """
    def findKthNumber(self, n: int, k: int) -> int:
        # 計算以 prefix 開頭的數字個數
        def count_smaller(prefix):
            cnt = 0
            cur, nxt = prefix, prefix + 1
            while cur <= n:
                cnt += min(n + 1, nxt) - cur
                cur *= 10
                nxt *= 10
            return cnt

        cur = 1
        k -= 1
        while k > 0:
            cnt = count_smaller(cur)
            print(n, k, cur, cnt, sep='\t')
            if k >= cnt:
                k -= cnt
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur
    
class Solution2:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_cnt(x, limit):
            a, b = str(x), str(limit)
            k = len(b) - len(a)
            ans = sum(10 ** i for i in range(k)) if k else 0
            ans += 10 ** k if (u := int(b[:len(a)])) > x else limit - x * 10 ** k + 1 if u == x else 0
            return ans

    
class Solution(Solution1):
    pass
# @lc code=end

sol = Solution()
print(sol.findKthNumber(13, 2)) # 10
print(sol.findKthNumber(1, 1)) # 1
print(sol.findKthNumber(10, 3)) # 2
print(sol.findKthNumber(10000, 10000)) # 9999

#
# @lcpr case=start
# 13\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

