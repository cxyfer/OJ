#
# @lc app=leetcode id=1442 lang=python3
# @lcpr version=30202
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. O(n^3)
        2. O(n^2)
        3. O(n) Hash Table
    """
    def countTriplets(self, arr: List[int]) -> int:
        # return self.solve1(arr)
        # return self.solve2(arr)
        # return self.solve3a(arr)
        return self.solve3b(arr)
    def solve1(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * (n + 1) # Prefix Sum
        for i, x in enumerate(arr):
            pre[i + 1] = pre[i] ^ x
        ans = 0
        for i in range(n): # i < j <= k
            for j in range(i + 1, n):
                for k in range(j, n):
                    # if pre[i] ^ pre[j] == pre[j] ^ pre[k + 1]:
                    if pre[i] == pre[k + 1]: # pre[j] is not important
                        ans += 1
        return ans
    def solve2(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * (n + 1) # Prefix Sum
        for i, x in enumerate(arr):
            pre[i + 1] = pre[i] ^ x
        ans = 0
        for i in range(n): # i < j <= k
            for k in range(i + 1, n):
                if pre[i] == pre[k + 1]: # j is not important
                    ans += k - i # (i, i+1, k), (i, i+2, k), ..., (i, k, k)
        return ans
    def solve3a(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * (n + 1) # Prefix Sum
        for i, x in enumerate(arr):
            pre[i + 1] = pre[i] ^ x
        pos = defaultdict(list)
        ans = 0
        for k in range(n):
            if pre[k + 1] in pos:
                for i in pos[pre[k + 1]]:
                    ans += k - i
            pos[pre[k]].append(k)
        return ans
    def solve3b(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * (n + 1) # Prefix Sum
        for i, x in enumerate(arr):
            pre[i + 1] = pre[i] ^ x
        cnt = Counter()
        tot = Counter()
        ans = 0
        for k in range(n):
            if pre[k + 1] in cnt:
                ans += cnt[pre[k + 1]] * k - tot[pre[k + 1]]
            cnt[pre[k]] += 1
            tot[pre[k]] += k
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,3,1,6,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n
# @lcpr case=end

#

