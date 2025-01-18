while True:
    S = int(input().strip())
    if S == 0:
        break
    N = int(input().strip())
    sets = []
    for _ in range(N):
        m, *stamps = map(int, input().strip().split())
        sets.append(stamps)

    cover = [0] * N
    for idx, stamps in enumerate(sets):
        n = len(stamps)
        mx = max(stamps)
        f = [float('inf')] * (mx * S + 1)
        for i in range(n + 1):
            f[0] = 0
        for j in range(1, mx * S + 1):
            for stamp in stamps:
                if j - stamp >= 0:
                    f[j] = min(f[j], f[j - stamp] + 1)
            if f[j] <= S:
                cover[idx] = j
            else:
                break
    candidates = []
    for i in range(N):
        candidates.append((i, cover[i], len(sets[i]), sorted(sets[i], reverse=True)))
    candidates.sort(key=lambda x: (-x[1], x[2], x[3]))
    ans = candidates[0][0]
    
    print(f"max coverage = {cover[ans]:>3} :", end='')
    for stamp in sets[ans]:
        print(f"{stamp:>3}", end='')
    print()