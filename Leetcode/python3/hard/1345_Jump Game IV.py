#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-end

"""
Similar:
- 3629. Minimum Jumps to Reach End via Prime Teleportation
- ABC436D Teleport Maze
"""

# @lc code=start
class Solution1:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)

        dist = [inf] * n
        dist[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            if u == n - 1:
                return dist[u]
            x = nums[u]
            for v in [u - 1, u + 1, *groups[x]]:
                if 0 <= v < n and dist[v] == inf:
                    dist[v] = dist[u] + 1
                    q.append(v)
                groups[x].clear()  # 注意這裡要清空，否則會 TLE
        return -1

class Solution2:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)
        
        m = len(groups)
        vals = list(groups.keys())
        v2i = {v: i for i, v in enumerate(vals, start=n)}

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
                if x in v2i:
                    v = v2i[x]
                    if dist[u] < dist[v]:
                        dist[v] = dist[u]
                        q.appendleft(v)  # 注意這裡用 appendleft
            else:  # 虛點
                for v in groups[vals[u - n]]:
                    if dist[u] + 1 < dist[v]:
                        dist[v] = dist[u] + 1
                        q.append(v)
        return -1

Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.minJumps([100,-23,-23,404,100,23,23,23,3,404]))  # 3