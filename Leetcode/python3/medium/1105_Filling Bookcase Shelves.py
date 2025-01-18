#
# @lc app=leetcode id=1105 lang=python3
# @lcpr version=30204
#
# [1105] Filling Bookcase Shelves
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
1. 動態規劃：選或不選
維護 books[i-1] 所在層的寬度 cur_w 和高度 cur_h
- 如果 books[i] 可以放到同一層，則選擇同一層
- 如果 books[i] 不可以放到同一層，則選擇下一層
O(n^2*shelfWidth)

2. 動態規劃：子問題
由前往後考慮，令 dfs(i) 為放置第 i+1 本書到第 n 本書的最小高度，
則可以枚舉該層的最後一本書 j ，以此遞迴到子問題 dfs(j+1)
"""
class Solution1:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        @cache
        def dfs(i, cur_w, cur_h):
            if i == n:
                return cur_h
            res = cur_h + dfs(i + 1, books[i][0], books[i][1]) # 放到下一層
            if cur_w + books[i][0] <= shelfWidth: # 可以放到同一層
                res = min(res, dfs(i + 1, cur_w + books[i][0], max(cur_h, books[i][1])))
            return res
        return dfs(0, 0, 0)
    
class Solution2:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        @cache
        def dfs(i):
            if i == n:
                return 0
            res = float('inf')
            max_h, left_w = 0, shelfWidth
            for j in range(i, n):
                left_w -= books[j][0]
                if left_w < 0: # 無法將 books[i], ... , books[j] 放到同一層
                    break
                max_h = max(max_h, books[j][1]) # 更新最大高度
                res = min(res, max_h + dfs(j + 1)) # 遞迴到子問題
            return res
        return dfs(0)
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[2,4],[3,2]]\n6\n
# @lcpr case=end

#

