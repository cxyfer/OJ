from collections import defaultdict

n, m = map(int, input().strip().split())
memories = []
for _ in range(n):
    r, v, s = input().strip().split()
    memories.append((int(r), int(v), s))

queries = []
for i in range(m):
    d, s = input().strip().split()
    queries.append((i, int(d), s))

# 有可能會 TLE
def solve1():
    class TrieNode:
        def __init__(self):
            self.child = defaultdict(TrieNode)
            self.memories = []

    root = TrieNode()
    for i, (r, v, s) in enumerate(memories):
        node = root
        for ch in s:
            node = node.child[ch]
            node.memories.append(i)

    for (i, d, s) in queries:
        node = root
        for ch in s:
            node = node.child[ch]
        ans = 0
        for idx in node.memories:
            if memories[idx][0] <= d:
                ans += memories[idx][1]
        print(ans)

def solve2():
    memories.sort(key=lambda x: x[0])
    queries.sort(key=lambda x: x[1])  # 離線詢問

    class TrieNode:
        def __init__(self):
            self.child = defaultdict(TrieNode)
            self.value = 0

    root = TrieNode()
    ans = [0] * m
    idx = 0
    for (i, d, s1) in queries:
        while idx < n and memories[idx][0] <= d:
            _, v, s2 = memories[idx]
            node = root
            for ch in s2:
                node = node.child[ch]
                node.value += v
            idx += 1

        node = root
        for ch in s1:
            node = node.child[ch]
        ans[i] = node.value

    print("\n".join(map(str, ans)))

# solve1()
solve2()