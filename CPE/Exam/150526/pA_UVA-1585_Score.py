t = int(input())

for kase in range(1, t + 1):
    s = input()
    ans = cur = 0
    for ch in s:
        if ch == "O":
            cur += 1
            ans += cur
        else:
            cur = 0
    print(ans)