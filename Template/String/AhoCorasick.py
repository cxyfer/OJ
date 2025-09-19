from typing import List
from collections import deque

"""
Aho-Corasick Automaton
令 u.goto[c] 表示在節點 u 時，匹配字元 c 後下一個節點，方便失配時直接跳到下一個可能匹配的位置，不用從 fail 往上找。
- 如果 u.child[c] 存在，則 u.goto[c] = u.child[c] 
- 如果 u.child[c] 不存在，則 u.goto[c] = u.fail.goto[c]
這裡直接用 child 當作 goto，但會破壞原本的 Trie 結構，需要注意。

Problem:
- 3213. Construct String with Minimum Cost
- 3292. Minimum Number of Valid Strings to Form Target II

Reference:
- https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917929/ac-zi-dong-ji-pythonjavacgo-by-endlessch-hcqk
"""

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None  # fail pointer
        self.last = None  # suffix link，用來快速跳到一定是某個 word 結尾的節點
        # self.is_end = False
        # self.depth = depth
        self.length = 0  # 可以取代 is_end 和 depth
        self.cost = float('inf')

class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str, cost: int):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                node.child[idx] = Node()
            node = node.child[idx]
        node.length = len(word)
        node.cost = min(node.cost, cost)  # 避免相同單字有不同 cost

    def build(self):  # O(|Σ|)，|Σ| 是字元集大小，n 是節點數，適合較稠密的 Trie 
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        for i, v in enumerate(self.root.child):
            if v is None:  
                self.root.child[i] = self.root  # 添加虛擬子節點
            else:
                v.fail = v.last = self.root
                q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None:
                    u.child[i] = u.fail.child[i]  # 添加虛擬子節點
                else:
                    v.fail = u.fail.child[i]  # 失配位置
                    v.last = v.fail if v.fail.length else v.fail.last  # 上一個一定是某個 word 結尾的節點
                    q.append(v)

    def build2(self):  # O(L)，L 是單字總長度，適合較稀疏的 Trie
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        for v in self.root.child:
            if v is None: continue
            v.fail = v.last = self.root
            q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None: continue
                fu = u.fail
                while fu != self.root and fu.child[i] is None:
                    fu = fu.fail
                if fu.child[i] is not None:
                    v.fail = fu.child[i]
                else:  # 如果一路找到根節點都沒有，則 fail 指向根
                    v.fail = self.root
                v.last = v.fail if v.fail.length else v.fail.last
                q.append(v)

    def traverse2(self, word: str):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('a')
            while node != self.root and node.child[idx] is None:
                node = node.fail
            if node.child[idx] is not None:
                node = node.child[idx]