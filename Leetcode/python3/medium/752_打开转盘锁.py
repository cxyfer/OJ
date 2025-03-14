#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
from preImport import *
# @lc code=start
class Solution:
    """
        四維空間下的 BFS
    """
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        def next(status: str) -> List[str]:
            lst = list(status)
            res = []
            for i in range(4):
                pre, nxt = (int(lst[i]) - 1) % 10, (int(lst[i]) + 1) % 10
                lst[i] = str(pre)
                res.append("".join(lst))
                lst[i] = str(nxt)
                res.append("".join(lst))
                lst[i] = status[i]
            return res

        q = deque([("0000", 0)])
        visited = {"0000"}
        while q:
            u, step = q.popleft()
            if u == target:
                return step
            for v in next(u):
                if v not in deadends and v not in visited:
                    q.append((v, step + 1))
                    visited.add(v)
        return -1
# @lc code=end
sol = Solution()
print(sol.openLock(["0201","0101","0102","1212","2002"],"0202")) # 6
print(sol.openLock(["8888"],"0009")) # 1
print(sol.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"],"8888")) # -1

