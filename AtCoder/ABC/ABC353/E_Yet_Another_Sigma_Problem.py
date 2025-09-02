"""
    Trie
    逐個插入字串，並計算每個節點的 cnt 值，代表有多少個字串經過該節點
"""
N = int(input())
S = input().split()

class Node:
    __slots__ = ['cnt', 'child']
    def __init__(self) -> None:
        self.cnt = 0
        self.child = [None] * 26

ans = 0
root = Node()
for s in S:
    cur = root
    for ch in s:
        v = ord(ch) - ord('a')
        if cur.child[v] == None: # Create a new node
            cur.child[v] = Node()
        cur = cur.child[v] # Move to the next node
        ans += cur.cnt # Add the number of strings that pass through this node
        cur.cnt += 1
print(ans)