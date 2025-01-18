from collections import deque

t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    lst = list(map(int, s))
    q = deque()
    for i in range(n - 1):
        q.append((i, i + 1))
    while q:
        i, j = q.popleft()
        if lst[j] == 0 or lst[j] - 1 <= lst[i]:
            continue
        lst[i], lst[j] = lst[j] - 1, lst[i]
        if i - 1 >= 0:
            q.append((i - 1, i))
        if j + 1 < n:
            q.append((j, j + 1))
    print(''.join(map(str, lst)))