n, q = map(int, input().split())

S = [""] + [input() for _ in range(n)]

for _ in range(q):
    op, *args = input().split()
    if op == "1":
        x, y, i = map(int, args)
        S[y] = S[y][:i] + S[x] + S[y][i:]
    elif op == "2":
        i = int(args[0])
        print(S[i])