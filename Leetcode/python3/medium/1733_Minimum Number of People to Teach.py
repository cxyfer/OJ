#
# @lc app=leetcode id=1733 lang=python3
#
# [1733] Minimum Number of People to Teach
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = list(map(set, languages))
        cnt = defaultdict(int)
        vis = set()
        for u, v in friendships:
            u, v = u - 1, v - 1
            if languages[u] & languages[v]:
                continue
            for x in [u, v]:
                if x in vis:
                    continue
                vis.add(x)
                for y in languages[x]:
                    cnt[y] += 1
        return len(vis) - (max(cnt.values()) if cnt else 0)
# @lc code=end
sol = Solution()
print(sol.minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]))  # 1
print(sol.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]))  # 2