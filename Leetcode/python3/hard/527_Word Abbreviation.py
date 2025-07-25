#
# @lc app=leetcode id=527 lang=python3
#
# [527] Word Abbreviation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
w1 = abbdef
w2 = abcdef

調整順序，把首尾移動到前面
w1 = af bcde
af bbde

相同長度才會有碰撞的問題，所以可以先依照長度分組，每組維護一個 trie
"""
# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.cnt = 0
        self.dist = -1
        self.idx = -1

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = [-1] * n
        
        # 相同長度才會有碰撞的問題，依照長度分組，每組維護一個 trie
        mp = defaultdict(list)
        for i, word in enumerate(words):
            abbr = word[0] + str(len(word) - 2) + word[-1] if len(word) > 3 else word
            mp[(len(word), abbr)].append(i)

        roots = defaultdict(TrieNode)
        def insert(word: str, idx: int) -> None:
            node = roots[len(word)]
            for i, c in enumerate(word):
                node = node.child[c]
                node.cnt += 1
                node.dist = len(word) - (i + 1)
                node.idx = idx

        for (_, abbr), idxs in mp.items():
            if len(idxs) > 1:
                for idx in idxs:
                    word = words[idx]
                    insert(word[0] + word[-1] + word[1:-1], idx)
            else:
                ans[idxs[0]] = abbr

        path = []
        def dfs(node: TrieNode) -> str:
            if node.cnt == 1 and len(path) >= 2:
                mid = str(node.dist) if node.dist > 1 else (list(node.child.keys())[0] if node.dist == 1 else "")
                abbr = path[0] + "".join(path[2:]) + mid + path[1]
                ans[node.idx] = abbr
                return
            for c in node.child:
                path.append(c)
                dfs(node.child[c])
                path.pop()
        for root in roots.values():
            dfs(root)
        return ans
# @lc code=end
sol = Solution()
print(sol.wordsAbbreviation(["like","god","internal","me","internet","interval","intension","face","intrusion"]))  # ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
print(sol.wordsAbbreviation(["aa","aaa"]))  # ["aa","aaa"]
print(sol.wordsAbbreviation(["meet","met"]))  # ["m2t","met"]
print(sol.wordsAbbreviation(["aa","aaa","aaaa","aaaaa"]))