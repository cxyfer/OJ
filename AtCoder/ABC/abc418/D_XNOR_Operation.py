N = int(input())
S = input()

ans = 0
f = [[0, 0] for _ in range(2)]
for i, c in enumerate(S):
    b = i & 1
    if c == '0':
        f[b][0] = f[b ^ 1][1]
        f[b][1] = f[b ^ 1][0] + 1
    else:
        f[b][0] = f[b ^ 1][0] + 1
        f[b][1] = f[b ^ 1][1]
    ans += f[b][0]
print(ans)