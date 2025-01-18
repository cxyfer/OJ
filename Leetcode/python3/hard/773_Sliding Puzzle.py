#
# @lc app=leetcode id=773 lang=python3
# @lcpr version=30204
#
# [773] Sliding Puzzle
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        DIR = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def get(status: str) -> List[str]:
            s = list(status)
            res = []
            x = s.index("0")
            for y in DIR[x]:
                s[x], s[y] = s[y], s[x]
                res.append("".join(s))
                s[x], s[y] = s[y], s[x]
            return res

        state = ""
        for row in board:
            for x in row:
                state += str(x)
        if state == "123450":
            return 0
        q = deque([(state, 0)])
        vis = set([state])
        while q:
            cur, d = q.popleft()
            if cur == "123450":
                return d
            for nxt in get(cur):
                if nxt in vis:
                    continue
                q.append((nxt, d + 1))
                vis.add(nxt)
        return -1
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,0,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,4,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,1,2],[5,0,3]]\n
# @lcpr case=end

#

