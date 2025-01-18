#
# @lc app=leetcode id=212 lang=python3
# @lcpr version=30203
#
# [212] Word Search II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Node: # Trie Node
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = Node() # Trie root
        for word in words:
            cur = root
            for ch in word:
                idx = ord(ch) - ord('a')
                if cur.children[idx] is None:
                    cur.children[idx] = Node()
                cur = cur.children[idx]
            cur.isEnd, cur.word = True, word

        ans = []
        def dfs(i: int, j: int, cur: Node):
            if cur.isEnd:
                ans.append(cur.word)
                cur.isEnd = False
            if i < 0 or i >= m or j < 0 or j >= n: # out of bound
                return
            ch = board[i][j]
            idx = ord(ch) - ord('a')
            if ch == '#' or cur.children[idx] is None: # visited or no match
                return
            board[i][j] = '#' # mark visited
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i+dx, j+dy, cur.children[idx])
            board[i][j] = ch # backtracking
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return ans
# @lc code=end

#
# @lcpr case=start
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["c","d"]]\n["abcb"]\n
# @lcpr case=end

#

