#
# @lc app=leetcode id=3485 lang=python3
#
# [3485] Longest Common Prefix of K Strings After Removal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedSet

class Node:
    def __init__(self, d: int):
        self.dep = d
        self.child = defaultdict(lambda: Node(d + 1))
        self.cnt = 0

    def __lt__(self, other):
        return self.dep < other.dep

    def __eq__(self, other):
        return self.dep == other.dep

    def __hash__(self):
        return hash(id(self))

class Trie:
    def __init__(self):
        self.root = Node(0)

    def insert(self, s: str):
        cur = self.root
        for ch in s:
            cur = cur.child[ch]
            cur.cnt += 1

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        st = SortedSet()  # {node}, compare by node.dep
        for word in words:
            cur = trie.root
            for ch in word:
                cur = cur.child[ch]
                if cur.cnt >= k:
                    st.add(cur)

        def calc(s: str) -> int:
            res = 0
            # Erase nodes of this path
            cur = trie.root
            for ch in s:
                cur = cur.child[ch]
                if cur.cnt >= k:
                    st.remove(cur)
                if cur.cnt >= k + 1:
                    res = max(res, cur.dep)

            # Find the longest common prefix
            if st:
                res = max(res, st[-1].dep)

            # Reinsert nodes of this path
            cur = trie.root
            for ch in s:
                cur = cur.child[ch]
                if cur.cnt >= k:
                    st.add(cur)
            return res

        return [calc(s) for s in words]
# @lc code=end

sol = Solution()
print(sol.longestCommonPrefix(["jump","run","run","jump","run"], 2))  # [3,4,4,3,4]
print(sol.longestCommonPrefix(["dog","racer","car"], 2))  # [0,0,0]
print(sol.longestCommonPrefix(["ecd","bcac","e"], 1))  # [4,3,4]