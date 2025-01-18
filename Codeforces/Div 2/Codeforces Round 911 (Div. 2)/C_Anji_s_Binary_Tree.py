from collections import deque

T = int(input())

ans = []

for tc in range(1, T+1):
    N = int(input())
    S = " " + input()
    TREE = [[-1, -1]] + [list(map(int, input().split())) for _ in range(N)]

    res = float('inf')
    q = deque([(1, 0)]) # (node, cnt)
    while q:
        node, cnt = q.pop()
        left, right = TREE[node] 
        if left == 0 and right == 0: # Leaf
            res = min(res, cnt)
            continue
        if left:
            q.append((left, cnt + (S[node] != 'L')))
        if right:
            q.append((right, cnt + (S[node] != 'R')))

    ans.append(res)
    
print(*ans, sep='\n')