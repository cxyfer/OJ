t = int(input())

for _ in range(t):
    s = input()
    ans = cur = 0
    for ch in s:
        if ch == "O":
            cur += 1
            ans += cur
        else:
            cur = 0
    print(ans)