from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m, q = map(int, input().split())

    ans = [0] * (m + 1)
    lvl = -1
    record = defaultdict(int)
    scr = m
    for _ in range(q):
        op, *args = map(int, input().split())
        if op == 1:
            lvl = args[0]
            record.clear()
            scr = m
        elif op == 2:
            idx, x = args
            if x != lvl or record[idx]:
                continue
            record[idx] = 1
            ans[idx] += scr
            scr -= 1
        else:
            idx, x = args
            if x != lvl or record[idx]:
                continue
            record[idx] = 2
    player = [(i, ans[i]) for i in range(1, m + 1)]
    player.sort(key=lambda x: (-x[1], x[0]))
    for idx, scr in player:
        print(idx, scr)