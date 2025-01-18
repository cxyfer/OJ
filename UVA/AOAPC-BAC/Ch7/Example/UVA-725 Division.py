kase = 0
while True:
    n = int(input().strip())
    if n == 0:
        break
    if kase > 0:
        print()
    kase += 1
    ans = []
    def dfs(i, s, cur):
        if cur * n > 98765: # 剪枝
            return
        if i == 5:
            x = n * cur
            for _ in range(5):
                j = x % 10
                if (1 << j) & s:
                    return
                x //= 10
                s |= 1 << j
            ans.append(cur)
            return
        # 枚舉下一個數字
        for j in range(10):
            if s & (1 << j):
                continue
            dfs(i + 1, s | (1 << j), cur * 10 + j)
    dfs(0, 0, 0)
    if len(ans) == 0:
        print(f"There are no solutions for {n}.")
    else:
        for x in ans:
            print(f"{n * x} / {x:05d} = {n}")