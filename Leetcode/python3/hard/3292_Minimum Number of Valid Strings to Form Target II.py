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
    __slot__ = ("child", "fail", "last", "is_end", "depth")

    def __init__(self, depth=0):
        self.child = [None] * 26
        self.fail = None  # fail pointer
        # self.last = None  # 本題不需要 last
        self.is_end = False
        self.depth = depth


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if not node.child[c]:
                node.child[c] = Node(node.depth + 1)
            node = node.child[c]
        node.is_end = True

    def build(self):  # O(|Σ|N)，N 是節點數；若 |Σ|=26 視為常數，則為 O(N) = O(L)
        self.root.fail = self.root
        # BFS
        q = deque()
        for i, v in enumerate(self.root.child):
            if v is None:
                # 添加虛擬子節點
                self.root.child[i] = self.root
            else:
                v.fail = self.root
                q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None:
                    # 添加虛擬子節點
                    u.child[i] = u.fail.child[i]
                else:
                    # 失配位置
                    v.fail = u.fail.child[i]
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
            c = ord(ch) - ord("a")
            node = node.child[c]
            # 沒有任何字串的前綴與 target[..i] 的後綴匹配
            if node is ac.root:
                return -1
            f[i] = f[i - node.depth] + 1
        return f[n]
# @lc code=end

sol = Solution()
print(sol.minValidStrings(["abc", "aaaaa", "bcdef"], "aabcdabc"))  # 3

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
