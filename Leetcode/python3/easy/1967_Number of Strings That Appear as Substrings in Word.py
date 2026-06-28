#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(p in word for p in patterns)


class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None
        self.cnt = 0


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if node.child[c] is None:
                node.child[c] = Node()
            node = node.child[c]
        node.cnt += 1

    def build(self):
        self.root.fail = self.root

        q = deque()
        for i in range(26):
            if self.root.child[i] is None:
                self.root.child[i] = self.root
            else:
                self.root.child[i].fail = self.root
                q.append(self.root.child[i])
        while q:
            u = q.popleft()
            for i in range(26):
                if u.child[i] is None:
                    u.child[i] = u.fail.child[i]
                else:
                    v = u.child[i]
                    v.fail = u.fail.child[i]
                    q.append(v)


class Solution2:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ac = AhoCorasick()
        for pattern in patterns:
            ac.insert(pattern)
        ac.build()

        ans = 0
        node = ac.root
        for ch in word:
            # 由於是 Trie 圖，直接轉移即可
            c = ord(ch) - ord("a")
            node = node.child[c]

            # 沿著 fail 鏈向上搜集所有匹配的模式串
            temp = node
            while temp is not ac.root and temp.cnt != -1:
                ans += temp.cnt
                # 標記為 -1，代表此節點已被統計過，避免重複計算
                temp.cnt = -1
                temp = temp.fail
        return ans


Solution = Solution1
# Solution = Solution2
# @lc code=end

