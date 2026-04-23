#
# @lc app=leetcode id=2452 lang=python3
#
# [2452] Words Within Two Edits of Dictionary
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            for word in dictionary:
                diff = 0
                for a, b in zip(query, word):
                    if a != b:
                        diff += 1
                        if diff > 2:
                            break
                else:
                    ans.append(query)
                    break
        return ans

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False

    def insert(self, word: str):
        node = self
        for c in word:
            if node.child[ord(c) - ord('a')] is None:
                node.child[ord(c) - ord('a')] = TrieNode()
            node = node.child[ord(c) - ord('a')]
        node.is_end = True

    def search(self, word: str, i: int, diff: int):
        if diff > 2:
            return False
        if i == len(word):
            return self.is_end
        c = ord(word[i]) - ord('a')
        for j in range(26):
            if self.child[j] is not None:
                if self.child[j].search(word, i + 1, diff + (j != c)):
                    return True
        return False


class Solution2:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        root = TrieNode()
        for word in dictionary:
            root.insert(word)

        ans = []
        for query in queries:
            if root.search(query, 0, 0):
                ans.append(query)
        return ans

# BASE = 26
MOD = int(1e18) + 3
BASE = randint(int(8e17), int(9e17))

class Solution3:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        P = [1] + [0] * n
        for i in range(n):
            P[i + 1] = P[i] * BASE % MOD

        # 生成修改次數 <= 1 的字串雜湊值
        def get_fuzzy(word: str):
            h = 0
            for c in reversed(word):
                h = (h * BASE + (ord(c) - ord('a'))) % MOD
            yield h
            for i, c1 in enumerate(word):
                for c2 in ascii_lowercase:
                    if c2 != c1:
                        h = (h + P[i] * (ord(c2) - ord(c1))) % MOD
                        yield h
                        h = (h - P[i] * (ord(c2) - ord(c1))) % MOD
        
        vis = set()
        for word in dictionary:
            for h in get_fuzzy(word):
                vis.add(h)
  
        ans = []
        for word in queries:
            # Meet in the middle
            for h in get_fuzzy(word):
                if h in vis:
                    ans.append(word)
                    break
        return ans

Solution = Solution1
# Solution = Solution2
# Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.twoEditWords(["word","note","ants","wood"], ["wood","joke","moat"]))  # ["word","note","wood"]