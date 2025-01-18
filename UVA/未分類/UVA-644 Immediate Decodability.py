import sys
def print(val=""): sys.stdout.write(str(val) + "\n")

class TrieNode:
    def __init__(self):
        self.child = [None] * 2
        self.cnt = 0
        self.is_end = False

    def insert(self, s):
        node = self
        for ch in s:
            idx = ord(ch) - ord('0')
            if node.child[idx] is None:
                node.child[idx] = TrieNode()
            node = node.child[idx]
        node.is_end = True
        node.cnt += 1

    def search_prefix(self, s):
        node = self
        for ch in s:
            if node.is_end:
                return True
            idx = ord(ch) - ord('0')
            node = node.child[idx]
        return node.cnt > 1
kase = 1
root = TrieNode()
words = []
ans = []
for line in sys.stdin:
    line = line.strip()
    if line == "9":
        flag = False
        for word in words:
            if root.search_prefix(word):
                flag = True
                break
        if flag:
            ans.append(f"Set {kase} is not immediately decodable")
        else:
            ans.append(f"Set {kase} is immediately decodable")
        kase += 1
        # reset
        root = TrieNode()
        words = []
    else:
        root.insert(line)
        words.append(line)

print("\n".join(ans))