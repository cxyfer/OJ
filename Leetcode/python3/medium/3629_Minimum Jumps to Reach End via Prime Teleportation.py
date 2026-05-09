#
# @lc app=leetcode id=3629 lang=python3
#
# [3629] Minimum Jumps to Reach End via Prime Teleportation
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
# @lc code=start
MAX_N = int(1e3 + 5)
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, math.isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False
primes = [x for x in range(2, MAX_N) if is_prime[x]]

class Solution1a:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            for p in primes:
                if p > x:
                    break
                if x % p == 0:
                    groups[p].append(i)
                    while x % p == 0:
                        x //= p
            if x > 1:
                groups[x].append(i)

        dist = [float('inf')] * n
        dist[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            if u == n - 1:
                return dist[u]
            for v in [u - 1, u + 1]:
                if 0 <= v < n and dist[v] == float('inf'):
                    dist[v] = dist[u] + 1
                    q.append(v)
            x = nums[u]
            if x in groups:
                for v in groups[x]:
                    if dist[v] == float('inf'):
                        dist[v] = dist[u] + 1
                        q.append(v)
                del groups[x]
        return -1

class Solution1b:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            for p in primes:
                if p > x:
                    break
                if x % p == 0:
                    groups[p].append(i)
                    while x % p == 0:
                        x //= p
            if x > 1:
                groups[x].append(i)
        
        m = len(groups)
        p2i = {p: i for i, p in enumerate(groups.keys(), start=n)}
        i2p = {i: p for p, i in p2i.items()}

        # 01 BFS
        dist = [float('inf')] * (n + m)
        dist[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            if u == n - 1:
                return dist[u]
            if u < n:
                for v in [u - 1, u + 1]:
                    if 0 <= v < n and dist[u] + 1 < dist[v]:
                        dist[v] = dist[u] + 1
                        q.append(v)
                x = nums[u]
                if x in p2i:
                    v = p2i[x]
                    if dist[u] < dist[v]:
                        dist[v] = dist[u]
                        q.appendleft(v)  # 注意這裡用 appendleft
            else:  # 虛點
                for v in groups[i2p[u]]:
                    if dist[u] + 1 < dist[v]:
                        dist[v] = dist[u] + 1
                        q.append(v)
        return -1

# Solution = Solution1a
Solution = Solution1b
# @lc code=end
sol = Solution()
print(sol.minJumps([1,2,4,6]))  # 2
print(sol.minJumps([4,6,5,8]))  # 3