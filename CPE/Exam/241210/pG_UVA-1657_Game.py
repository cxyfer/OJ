from collections import defaultdict

while True:
    try:
        N, M = map(int, input().strip().split())
    except:
        break

    s_cnt = [0] * (2 * N)
    p_cnt = [0] * (N * (N - 1) + 1)

    used = [[True] * (N + 1) for _ in range(N + 1)]
    for x in range(1, N + 1):
        for y in range(x + 1, N + 1):
            used[x][y] = False
            s_cnt[x + y] += 1
            p_cnt[x * y] += 1
    
    for i in range(1, M + 1):
        for x in range(1, N + 1):
            for y in range(x + 1, N + 1):
                if used[x][y]:
                    continue
                prod = x * y
                sum_ = x + y
                if i & 1:
                    if s_cnt[sum_] == 1:
                        used[x][y] = True
                        s_cnt[sum_] -= 1
                        p_cnt[prod] -= 1
                else:
                    if p_cnt[prod] == 1:
                        used[x][y] = True
                        p_cnt[prod] -= 1
                        s_cnt[sum_] -= 1

    ans = []
    for x in range(1, N + 1):
        for y in range(x + 1, N + 1):
            if used[x][y]:
                continue
            if M & 1:
                if p_cnt[x * y] == 1:
                    ans.append((x, y))
            else: # 最後是 B 說我知道了
                if s_cnt[x + y] == 1:
                    ans.append((x, y))

    print(len(ans))
    for (x, y) in ans:
        print(f"{x} {y}")