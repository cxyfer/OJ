N, Q = map(int, input().split())

class Node:
    def __init__(self, word = "", pre = None) -> None:
        self.word = word
        self.pre = pre

nodes = [None for _ in range(N + 1)]
for _ in range(Q):
    op, p, *args = input().split()
    op, p = int(op), int(p)
    if op == 1:
        nodes[p] = nodes[0]
    elif op == 2:
        s = args[0]
        nodes[p] = Node(s, nodes[p])
    else:
        nodes[0] = nodes[p]

ans = []
node = nodes[0]
while node:
    ans.append(node.word)
    node = node.pre
ans.reverse()
print(''.join(ans))