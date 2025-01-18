#
# @lc app=leetcode id=2097 lang=python3
# @lcpr version=30204
#
# [2097] Valid Arrangement of Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
Eulerian Path
Hierholzer's Algorithm
"""
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        n = len(pairs)
        cnt = defaultdict(int)
        g = defaultdict(deque)
        for idx, (x, y) in enumerate(pairs):
            cnt[x] += 1
            cnt[y] -= 1
            g[x].append((y, idx))

        st = pairs[0][0]
        for x, v in cnt.items():
            if v == 1:
                st = x
                break

        path = []
        used = [False] * n
        def dfs(u):
            while len(g[u]):
                v, idx = g[u].pop()
                if used[idx]:
                    continue
                used[idx] = True
                dfs(v)
            path.append(u)
        dfs(st)

        ans = []
        for x, y in pairwise(reversed(path)):
            ans.append([x, y])
        return ans
# @lc code=end

sol = Solution()
print(sol.validArrangement([[5,1],[4,5],[11,9],[9,4]]))
# print(sol.validArrangement([[1,3],[3,2],[2,1]]))
# print(sol.validArrangement([[1,2],[1,3],[2,1]]))
# print(sol.validArrangement([[8,5],[8,7],[0,8],[0,5],[7,0],[5,0],[0,7],[8,0],[7,8]]))

#
# @lcpr case=start
# [[5,1],[4,5],[11,9],[9,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[3,2],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,3],[2,1]]\n
# @lcpr case=end

#

