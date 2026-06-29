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


class Solution2:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(word)
        ans = 0
        for t in patterns:
            m = len(t)
            pi = [0] * m
            ln = 0
            for i in range(1, m):
                while ln and t[i] != t[ln]:
                    ln = pi[ln - 1]
                if t[i] == t[ln]:
                    ln += 1
                pi[i] = ln

            ln = 0
            for i in range(n):
                while ln and word[i] != t[ln]:
                    ln = pi[ln - 1]
                if word[i] == t[ln]:
                    ln += 1
                if ln == m:
                    ans += 1
                    break
        return ans


class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None  # fail pointer
        self.last = None  # suffix link，用來快速跳到一定是某個 word 結尾的節點
        # self.is_end = False
        # self.depth = depth
        self.length = 0  # 可以取代 is_end 和 depth
        self.cnt = 0  # 記錄有多少個 pattern 匹配到此節點


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if not node.child[c]:
                node.child[c] = Node()
            node = node.child[c]
        node.length = len(word)
        node.cnt += 1  # 記錄有多少個 pattern 匹配到此節點

    def build(self):  # O(|Σ|N)，N 是節點數；若 |Σ|=26 視為常數，則為 O(N) = O(L)
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        for i, v in enumerate(self.root.child):
            if v is None:
                # 添加虛擬子節點
                self.root.child[i] = self.root
            else:
                v.fail = v.last = self.root
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
                    # 上一個一定是某個 word 結尾的節點
                    v.last = v.fail if v.fail.length else v.fail.last
                    q.append(v)


class Solution3:
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

            # 沿著 fail 或 last 鏈向上搜集所有匹配的模式串
            temp = node
            while temp is not ac.root and temp.cnt != -1:
                ans += temp.cnt
                # 標記為 -1，代表此節點已被統計過，避免重複計算
                temp.cnt = -1
                # temp = temp.fail
                temp = temp.last
        return ans


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

