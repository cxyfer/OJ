#
# @lc app=leetcode id=1298 lang=python3
#
# [1298] Maximum Candies You Can Get from Boxes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        hasBox = [False] * n
        canOpen = [False] * n
        visited = [False] * n

        q = deque()
        for u in initialBoxes:
            hasBox[u] = True
        for u in range(n):
            if status[u] == 1:
                canOpen[u] = True
            if hasBox[u] and canOpen[u]:
                visited[u] = True
                q.append(u)
        ans = 0
        while q:
            u = q.popleft()
            ans += candies[u]
            for v in containedBoxes[u]:
                hasBox[v] = True
                if hasBox[v] and canOpen[v] and not visited[v]:
                    visited[v] = True
                    q.append(v)
            for v in keys[u]:
                canOpen[v] = True
                if hasBox[v] and canOpen[v] and not visited[v]:
                    visited[v] = True
                    q.append(v)
        return ans  
# @lc code=end

