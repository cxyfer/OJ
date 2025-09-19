#
# @lc app=leetcode id=3292 lang=python3
# @lcpr version=30204
#
# [3292] Minimum Number of Valid Strings to Form Target II
#


# @lcpr-template-start
from preImport import *
import random
# @lcpr-template-end
"""
1. Hash String
2. Aho-Corasick Automaton
"""
# @lc code=start
class Node:
    def __init__(self, depth: int = 0):
        self.child = [None] * 26
        # goto[i] 表示當前節點匹配字元 i 後下一個節點，方便失配時直接跳到下一個可能匹配的位置
        self.goto = [None] * 26  
        self.isEnd = False
        self.depth = depth
        self.fail = None  # fail pointer

class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                node.child[idx] = Node(node.depth + 1)
            node = node.child[idx]
        node.isEnd = True

    def build(self):
        self.root.fail = self.root
        # BFS
        q = deque()
        for i, v in enumerate(self.root.child):
            if v is None:
                # self.root.child[i] = self.root
                self.root.goto[i] = self.root
            else:
                # v.fail = self.root
                self.root.goto[i] = v
                self.root.goto[i].fail = self.root
                q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None:
                    # u.child[i] = u.fail.child[i]
                    u.goto[i] = u.fail.goto[i]
                else:
                    # v.fail = u.fail.child[i]
                    u.goto[i] = v
                    u.goto[i].fail = u.fail.goto[i]
                    q.append(v)

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        ac = AhoCorasick()
        for word in words:
            ac.insert(word)
        ac.build()

        n = len(target)
        f = [0] * (n + 1)
        node = ac.root
        for i, ch in enumerate(target, 1):
            # node = node.child[ord(ch) - ord('a')]
            node = node.goto[ord(ch) - ord('a')]
            # 沒有任何字串的前綴與 target[..i] 的後綴匹配
            if node is ac.root:
                return -1
            f[i] = f[i - node.depth] + 1
        return f[n]
# @lc code=end

sol = Solution()
print(sol.minValidStrings(["abc","aaaaa","bcdef"], "aabcdabc"))  # 3

#
# @lcpr case=start
# ["abc","aaaaa","bcdef"]\n"aabcdabc"\n
# @lcpr case=end

# @lcpr case=start
# ["abababab","ab"]\n"ababaababa"\n
# @lcpr case=end

# @lcpr case=start
# ["abcdef"]\n"xyz"\n
# @lcpr case=end

#

