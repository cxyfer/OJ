from typing import List
from collections import deque

"""
Aho-Corasick Automaton
令 u.goto[c] 表示在節點 u 時，匹配字元 c 後下一個節點，方便失配時直接跳到下一個可能匹配的位置，不用從 fail 往上找。
- 如果 u.child[c] 存在，則 u.goto[c] = u.child[c] 
- 如果 u.child[c] 不存在，則 u.goto[c] = u.fail.goto[c]
這裡直接用 child 當作 goto，但會破壞原本的 Trie 結構，需要注意。

fail 指標有個性質是可以構成一棵樹，稱為 fail tree，根節點是 root，其他節點的父節點是它的 fail 指向的節點。
因為 fail 只會指向深度比自己淺的節點，所以 fail tree 是一棵樹。

Template:
- P3808 AC 自动机（简单版）
  因為只是問有沒有出現，因此只需要延 fail tree 往上找，並標記 fail tree 上訪問過的節點，避免二次訪問即可。
- P3796 AC 自动机（简单版 II）
  要統計出現次數，因為有些節點不是某個 word 的結尾，沿著 fail tree 往上找會浪費時間，
  又因為要統計出現次數不能直接標記，這時候就要使用 last 指標跳過沒有用的節點。
  另外因為要統計出現次數，本題需要保留每個 word 對應的節點。
- P5357 【模板】AC 自动机.py
  但是就算使用 last 指標，沿著 last 指標往上找最壞可以是 O(n)，其中 n 是模式串的數量，在模式串太多的情況下，也會浪費時間。
  比較好的做法是不直接每次都往上找，而是先把所有節點按照 fail tree 的拓撲順序排序，
  然後從後往前統計出現次數並累加貢獻，這樣每個節點只會被訪問一次。

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


class AhoCorasick:
    def __init__(self):
        self.root = Node()
        # self.nodes = []  # 保留每個 word 對應的節點

    def insert(self, word: str):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if not node.child[c]:
                node.child[c] = Node()
            node = node.child[c]
        node.length = len(word)
        # self.nodes.append(node)  # 保留每個 word 對應的節點

    def build(self):  # O(|Σ|N)，N 是節點數；若 |Σ|=26 視為常數，則為 O(N) = O(L)
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        # order = []  # 用來保存 fail tree 的拓撲順序
        for i, v in enumerate(self.root.child):
            if v is None:
                # 添加虛擬子節點
                self.root.child[i] = self.root
            else:
                v.fail = v.last = self.root
                q.append(v)
                # order.append(v)
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
                    # order.append(v)
        # self.order = order

    def build2(self):  # 最壞 O(|Σ|N + L^2)；若 fail 回退很少，實務上接近 O(|Σ|N)
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        for v in self.root.child:
            if v is None:
                continue
            v.fail = v.last = self.root
            q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None:
                    continue
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
            idx = ord(ch) - ord("a")
            while node != self.root and node.child[idx] is None:
                node = node.fail
            if node.child[idx] is not None:
                node = node.child[idx]


class Solution3213:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        ac = AhoCorasick()

        def insert(self, word: str, cost: int):
            node = self.root
            for ch in word:
                c = ord(ch) - ord("a")
                if not node.child[c]:
                    node.child[c] = Node()
                node = node.child[c]
            node.length = len(word)
            if not hasattr(node, "cost"):
                node.cost = cost
            else:
                node.cost = min(node.cost, cost)  # 避免相同單字有不同 cost

        ac.insert = insert.__get__(ac)  # 綁定方法到 ac 實例

        for word, cost in zip(words, costs):
            ac.insert(word, cost)
        ac.build()

        n = len(target)
        f = [0] + [float("inf")] * n
        node = ac.root
        for i, ch in enumerate(target, 1):
            node = node.child[ord(ch) - ord("a")]
            if node.length:  # 匹配到了一個盡可能長的 words[k]
                f[i] = min(f[i], f[i - node.length] + node.cost)
            # 沿著 last 往上尋找，可能可以找到其餘更短，但可以使成本更小的 words[k]
            temp = node.last
            while temp != ac.root:
                f[i] = min(f[i], f[i - temp.length] + temp.cost)
                temp = temp.last
        return f[n] if f[n] != float("inf") else -1


sol = Solution3213()
print(
    sol.minimumCost("abcdef", ["abdef", "abc", "d", "def", "ef"], [100, 1, 1, 10, 5])
)  # 7
