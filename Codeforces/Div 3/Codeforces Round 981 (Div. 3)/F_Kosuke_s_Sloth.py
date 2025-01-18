MOD = 10**9 + 7

pisano = {1: (1, 1, [1])}
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    if k not in pisano:
        f_pre, f_cur = 1, 1
        pos = []
        i = 1
        while True:
            if f_pre % k == 0:
                pos.append(i)
            f_pre, f_cur = f_cur, (f_pre + f_cur) % k
            i += 1
            if f_pre == 1 and f_cur == 1:
                ln = i - 1
                break
        pisano[k] = (ln, len(pos), pos)

    ln, cnt, pos = pisano[k]
    if cnt == 0:
        print(-1)
        continue
    q, r = divmod(n, cnt)
    if r == 0:
        index = (q * ln) % MOD
    else:
        index = ((q * ln) + pos[r-1]) % MOD
    print(index)