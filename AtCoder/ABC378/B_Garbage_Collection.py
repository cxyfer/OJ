N = int(input())
garbages = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
for _ in range(Q):
    t_j, d_j = map(int, input().split())
    q_i, r_i = garbages[t_j - 1]
    if d_j % q_i == r_i:
        ans = d_j
    else:
        ans = d_j + ((r_i - d_j) % q_i)
    print(ans)