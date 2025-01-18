#
# @lc app=leetcode id=676 lang=python3
# @lcpr version=30204
#
# [676] Implement Magic Dictionary
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Trie:  # Trie Node
    def __init__(self):
        self.child = {}
        self.is_end = False

class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.root
            for ch in word:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
            cur.is_end = True

    def search(self, searchWord: str) -> bool:
        def dfs(node: Trie, i: int, modified: bool) -> bool:
            if i == len(searchWord):
                return modified and node.is_end

            if searchWord[i] in node.child:  # 不修改當前位置的字母
                if dfs(node.child[searchWord[i]], i + 1, modified):
                    return True

            if not modified:  # 嘗試修改當前位置的字母，但只能修改一次
                for ch in node.child:  # 只需要考慮在 Trie 中存在的字母即可
                    if ch == searchWord[i]:
                        continue
                    if dfs(node.child[ch], i + 1, True):
                        return True

            return False

        return dfs(self.root, 0, False)
        
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end



