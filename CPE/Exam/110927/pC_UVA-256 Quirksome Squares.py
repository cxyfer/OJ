squares = []
for i in range(10000):
    squares.append(i * i)

ans = [[] for _ in range(9)] # 2, 4, 6, 8

for ln in range(2, 9, 2):
    for x in squares:
        if x >= 10 ** ln:
            break
        a, b = divmod(x, 10 ** (ln // 2))
        if (a + b) ** 2 == x:
            ans[ln].append(x)

while True:
    try:
        n = int(input())
    except EOFError:
        break
    for x in ans[n]:
        print(f"{x:0{n}d}")