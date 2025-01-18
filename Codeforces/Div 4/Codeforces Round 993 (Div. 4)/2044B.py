t = int(input())

for _ in range(t):
    s = input()
    ans = [""] * len(s)
    for i, ch in enumerate(s):
        if ch == "p":
            ans[i] = "q"
        elif ch == "q":
            ans[i] = "p"
        else:
            ans[i] = ch
    ans.reverse()
    print("".join(ans))