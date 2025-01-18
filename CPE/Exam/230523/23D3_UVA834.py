while True:
    try:
        x, y = map(int, input().split())
    except EOFError:
        break
    ans = []
    while y:
        ans.append(x // y)
        x, y = y, x % y
    print(f"[{ans[0]}", end = "")
    if len(ans) > 1:
        print(";", end = "")
        print(','.join(map(str, ans[1:])), end = "")
    print("]")
