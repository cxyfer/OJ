while True:
    try:
        s, t = input().split()
    except EOFError:
        break
    j = 0
    for i, ch in enumerate(t):
        if ch == s[j]:
            j += 1
            if j == len(s):
                break
    print("Yes" if j == len(s) else "No")