n = int(input())
teams = [input() for _ in range(n)]
m = int(input())
bans = [input() for _ in range(m)]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

root = TrieNode()

for ban in bans:
    cur = root
    for ch in ban:
        if ch not in cur.children:
            cur.children[ch] = TrieNode()
        cur = cur.children[ch]
    cur.is_end = True

for team in teams:
    flag = False
    for i in range(len(team)):
        if flag:
            break
        cur = root
        for j in range(i, len(team)):
            if team[j] not in cur.children:
                break
            cur = cur.children[team[j]]
            if cur.is_end:
                flag = True
                break
    print("Yes" if flag else "No")