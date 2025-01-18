#
# @lc app=leetcode id=3377 lang=python3
# @lcpr version=30204
#
# [3377] Digit Operations to Make Two Integers Equal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
N = int(1e4 + 5)
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i * i, N, i):
            is_prime[j] = False

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        if is_prime[n] or is_prime[m]:
            return -1
        src = str(n)
        tgt = str(m)
        ln = len(src)

        dist = defaultdict(lambda: float('inf'))
        dist[src] = n
        hp = []
        heappush(hp, (n, src))  # (cost, state)
        while hp:
            d, cur = heappop(hp)
            if dist[cur] < d:
                continue
            if cur == tgt:
                return d
            lst = list(map(int, cur))
            nexts = []
            for i in range(ln):
                if lst[i] < 9: # +1
                    n_lst = lst[:]
                    n_lst[i] += 1
                    nexts.append("".join(map(str, n_lst)))
                if lst[i] > 0: # -1
                    if lst[0] == 0 or i == 0 and lst[i] == 1: # 不能有前導 0
                        continue
                    n_lst = lst[:]
                    n_lst[i] -= 1
                    nexts.append("".join(map(str, n_lst)))
            for nxt in nexts:
                val = int(nxt)
                if is_prime[val]:
                    continue
                nd = d + val
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    heappush(hp, (nd, nxt))
        return -1
# @lc code=end

sol = Solution()
print(sol.minOperations(n = 10, m = 12)) # 85
print(sol.minOperations(n = 4, m = 8)) # -1
print(sol.minOperations(n = 6, m = 2)) # -1
print(sol.minOperations(n = 5637, m = 2034)) # 34943

#
# @lcpr case=start
# 10\n12\n
# @lcpr case=end

# @lcpr case=start
# 4\n8\n
# @lcpr case=end

# @lcpr case=start
# 6\n2\n
# @lcpr case=end

#

