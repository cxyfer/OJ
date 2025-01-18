from collections import deque

while True:
    n = int(input())
    if n == 0:
        break
    q = deque(range(1, n + 1))
    discarded = []
    while len(q) >= 2:
        discarded.append(q.popleft())
        q.append(q.popleft())
    if discarded:
        print(f"Discarded cards: {', '.join(map(str, discarded))}")
    else:
        print("Discarded cards:")
    print(f"Remaining card: {q[0]}")