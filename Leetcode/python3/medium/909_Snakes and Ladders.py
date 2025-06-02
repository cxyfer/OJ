#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_pos(u: int) -> tuple[int, int]:
            r, c = divmod(u - 1, n)
            if r & 1:
                return n - 1 - r, n - 1 - c
            else:
                return n - 1 - r, c
        q = deque([(1, 0)])
        vis = set([1])
        while q:
            u, d = q.popleft()
            r, c = get_pos(u)
            if board[r][c] != -1:
                u = board[r][c]
            if u == n * n:
                return d
            for v in range(u + 1, min(u + 6, n * n) + 1):
                if v in vis:
                    continue
                vis.add(v)
                q.append((v, d + 1))
        return -1
# @lc code=end

