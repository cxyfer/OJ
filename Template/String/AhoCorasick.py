from typing import List
from collections import deque

"""
    Aho-Corasick Automaton

    Problem:
    - 3213. Construct String with Minimum Cost
    - 3292. Minimum Number of Valid Strings to Form Target II

    Reference:
    - https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917929/ac-zi-dong-ji-pythonjavacgo-by-endlessch-hcqk
"""

class Node:
    def __init__(self):
        self.child = [None] * 26
        # self.is_end = False
        # self.depth = depth
        self.length = 0 # 若只保存在結尾的節點，可以省略 is_end
        self.fail = None # fail pointer
        self.last = None # suffix link，用來快速跳到一定是某個 word 結尾的節點
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
        node.cost = min(node.cost, cost) # 避免相同單字有不同 cost

    def build(self):
        self.root.fail = self.root.last = self.root
        q = deque()
        # 先處理第一層的 fail 和 last
        for i, child in enumerate(self.root.child):
            if child is None: # 添加虛擬子節點
                self.root.child[i] = self.root
            else:
                child.fail = child.last = self.root # 第一層的失配指標都指向 root
                q.append(child)
        # BFS
        while q:
            node = q.popleft()
            for i, child in enumerate(node.child):
                if child is None: # 添加虛擬子節點
                    # 虛擬子節點 node.child[i] 和 node.fail.child[i] 是同一個
                    # 方便失配時直接跳到下一個可能匹配的位置（但不一定是某個 words[k] 的最后一個字母）
                    node.child[i] = node.fail.child[i]
                    continue
                # 計算失配位置
                child.fail = node.fail.child[i] 
                # 計算 suffix link，沿著 fail 指標找到一定是某個 word 結尾的節點
                child.last = child.fail if child.fail.length else child.fail.last
                q.append(child)