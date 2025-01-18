while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    ans = list()
    vis = dict()
    print(f"{a}/{b} = {a//b}.", end="")
    a %= b
    a *= 10
    while a not in vis:
        vis[a] = len(ans)
        ans.append(a//b)
        a %= b
        a *= 10
    for i in range(min(50, len(ans))):
        if i == vis[a]:
            print("(", end="")
        print(ans[i], end="")
    if len(ans) > 50:
        print("...", end="")
    print(")")
    print(f"   {len(ans) - vis[a]} = number of digits in repeating cycle")
    print()