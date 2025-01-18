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
# @lc code=start
"""
    1. Hash String
    2. Aho-Corasick Automaton
"""
class Node:
    def __init__(self, depth: int = 0):
        self.child = [None] * 26
        self.isEnd = False
        self.depth = depth
        self.fail = None # fail pointer

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
        q = deque()
        for i, child in enumerate(self.root.child):
            if child is None:
                self.root.child[i] = self.root
            else:
                child.fail = self.root
                q.append(child)
        # BFS
        while q:
            node = q.popleft()
            for i, child in enumerate(node.child):
                if child is None:
                    # node.child[i] 和 node.fail.child[i] 是同一個虛擬子節點
                    # 方便失配時直接跳到下一個可能匹配的位置（但不一定是某個 words[k] 的最后一個字母）
                    node.child[i] = node.fail.child[i]
                else:
                    child.fail = node.fail.child[i]  # 计算失配位置
                    q.append(child)

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
            # 如果沒有匹配相當於移動到 fail 的 child[ch]
            node = node.child[ord(ch) - ord('a')]
            # 沒有任何字串的前綴與 target[..i] 的後綴匹配
            if node is ac.root:
                return -1
            f[i] = f[i - node.depth] + 1
        return f[n]
# @lc code=end



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

