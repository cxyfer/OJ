from collections import deque

Q = int(input())
snakes = deque()
s = 0  # 減少的長度總和
for _ in range(Q):
    op, *args = map(int, input().split())
    if op == 1:
        h = snakes[-1][0] + snakes[-1][1] if snakes else 0
        l = args[0]
        snakes.append((h, l))
    elif op == 2:
        _, m = snakes.popleft()
        s += m
    else:
        k = args[0] - 1  # 0-based
        print(snakes[k][0] - s)