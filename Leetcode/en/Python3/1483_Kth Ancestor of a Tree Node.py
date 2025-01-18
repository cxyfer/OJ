# @algorithm @lc id=1296 lang=python3 
# @title kth-ancestor-of-a-tree-node
from en.Python3.mod.preImport import *

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length() - 1
        pa = [[p] + [-1] * m for p in parent] # pa[i][j] 表示 i 的第 2^j 個祖先
        for i in range(m):
            for x in range(n):
                if pa[x][i] != -1:
                    p = pa[x][i]
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1: # k 的第 i 位是 1
                node = self.pa[node][i]
                if node == -1:
                    break
        return node

    # 另一種寫法，不斷去掉 k 的最低位 1
    def getKthAncestor2(self, node: int, k: int) -> int:
        while k and node != -1: 
            lb = k & -k # k 的最低位 1
            node = self.pa[node][lb.bit_length() - 1]
            k ^= lb
        return node