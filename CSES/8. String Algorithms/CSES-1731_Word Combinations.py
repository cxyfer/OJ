"""
    Trie DP

    Python TLE
"""
import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False

MOD = 10 ** 9 + 7
s = input().strip()
n = len(s)
root = TrieNode()
k = int(input())
for _ in range(k):
    w = input().strip()
    node = root
    for ch in w:
        idx = ord(ch) - ord('a')
        if node.child[idx] is None:
            node.child[idx] = TrieNode()
        node = node.child[idx]
    node.is_end = True

f = [0] * (n + 1)
f[n] = 1
for i in range(n - 1, -1, -1):
    node = root
    for j in range(i, n):
        idx = ord(s[j]) - ord('a')
        if node.child[idx] is None:
            break
        node = node.child[idx]
        if node.is_end:
            f[i] = (f[i] + f[j + 1]) % MOD
print(f[0])
