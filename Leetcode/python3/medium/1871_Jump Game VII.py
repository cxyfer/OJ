#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        # @cache
        # def dfs(i: int) -> bool:
        #     if i == 0:
        #         return True
        #     if s[i] == '1':
        #         return False
        #     for j in range(i - minJump, max(i - maxJump - 1, -1), -1):
        #         if dfs(j):
        #             return True
        #     return False

        # return dfs(n - 1)

        f = [False] * n
        f[0] = True
        q = deque([0])
        for i, ch in enumerate(s):
            if ch == "1":
                continue
            while q and q[0] < i - maxJump:
                q.popleft()
            if q and q[0] <= i - minJump:
                f[i] = True
                q.append(i)
        return f[n - 1]


class Solution1b:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] == "1":
            return False

        q = deque([0])
        for i in range(minJump, n):
            if s[i] == "1":
                continue
            while q and q[0] < i - maxJump:
                q.popleft()
            if not q:
                return False
            if q[0] <= i - minJump:
                q.append(i)
        return len(q) > 0 and q[-1] == n - 1


class Solution2:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] == "1":
            return False

        diff = [0] * (n + 1)
        diff[0] = 1
        diff[1] = -1
        sum_d = 0
        for i, ch in enumerate(s):
            sum_d += diff[i]
            if ch == "0" and sum_d > 0:
                diff[min(i + minJump, n)] += 1
                diff[min(i + maxJump + 1, n)] -= 1
        return sum_d > 0


class Solution3:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] == "1":
            return False

        f = [False] * n
        f[0] = True

        j = 0
        for i, ch in enumerate(s):
            if ch == "1" or not f[i]:
                continue
            U = min(i + maxJump, n - 1)
            j = max(j, i + minJump)
            while j <= U:
                f[j] = True
                j += 1
            if j == n:
                break
        return f[n - 1]


# Solution = Solution1
Solution = Solution1b
# Solution = Solution2
# Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.canReach("011010", 2, 3))  # true
print(sol.canReach("00111010", 3, 5))  # false