from collections import defaultdict
import sys
sys.setrecursionlimit(int(3e5 + 5))

class TrieNode:
    __slots__ = ['child', 'nodes']
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.nodes = []

def solve():
    n = int(input())

    root = TrieNode()

    mp = [None] * (n + 1)
    mp[0] = root
    for u in range(1, n + 1):
        fa, y = map(int, input().split())
        mp[u] = mp[fa].child[y]
        mp[u].nodes.append(u)

    ans = []

    # def dfs(u: TrieNode):
    #     ans.extend(u.nodes)  # u.nodes 必定有序
    #     for _, v in sorted(u.child.items(), key=lambda x: x[0]):
    #         dfs(v)
    # dfs(root)

    st = [(root, 0)]
    while st:
        u, i = st.pop()
        if i == 0:
            ans.extend(u.nodes)
            u.child = sorted(u.child.items(), key=lambda x: x[0])
        for j in range(i, len(u.child)):
            v = u.child[j][1]
            st.append((u, i + 1))
            st.append((v, 0))
            break

    print(*ans)

if __name__ == "__main__":
    solve()