# @algorithm @lc id=1753 lang=python3 
# @title path-with-minimum-effort


from en.Python3.mod.preImport import *
# @test([[1,2,2],[3,8,2],[5,3,5]])=2
# @test([[1,2,3],[3,8,4],[5,3,5]])=1
# @test([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])=0
class Solution:
    """
        BFS + Binary Search
    """
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        left, right = 0, 10**6
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            q = deque([(0, 0)])
            visited = {(0, 0)} 
            while q:
                x, y = q.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        if abs(heights[x][y] - heights[nx][ny]) <= mid:
                            q.append((nx, ny))
                            visited.add((nx, ny))
            
            if (m - 1, n - 1) in visited: # can reach the end
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans