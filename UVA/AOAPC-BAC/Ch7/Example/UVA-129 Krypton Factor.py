from string import ascii_uppercase

while True:
    n, L = map(int, input().split())
    if n == 0 and L == 0:
        break
    C = ascii_uppercase[:L]

    def check(path):
        for k in range(1, len(path) // 2 + 1):
            if path[-k:] == path[-2 * k:-k]:
                return False
        return True

    cnt = 0
    ans = []
    path = []
    def dfs(i):
        global cnt, ans
        if cnt == n:
            ans = path[:]
            return
        for ch in C:
            path.append(ch)
            if check(path):
                cnt += 1
                dfs(i + 1)
                if cnt == n:
                    return
            path.pop()
    dfs(0)
    for i, ch in enumerate(ans, 1):
        print(ch, end="")
        if len(ans) > 64 and i % 64 == 0:
            print()
        elif i < len(ans) and i % 4 == 0:
            print(" ", end="")
    print()
    print(len(ans))
