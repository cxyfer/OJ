x, n = map(int, input().split())
P = list(map(int, input().split()))

pos = [0] + sorted(P) + [x]
ln = len(pos)

# Doubly Linked List
adj = {pos[i]: [pos[i - 1], pos[i + 1]] for i in range(1, ln - 1)}
adj[0] = [0, pos[1]]
adj[x] = [pos[-2], x]

mx = max(pos[i] - pos[i - 1] for i in range(1, ln))
ans = []
for p in reversed(P):
    ans.append(mx)
    left, right = adj.pop(p)
    mx = max(right - left, mx)
    adj[left][1] = right
    adj[right][0] = left

print(*ans[::-1])