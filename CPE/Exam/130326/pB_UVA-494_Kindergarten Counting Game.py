while True:
    try:
        s = input()
    except EOFError:
        break

    ans = cur = 0
    for ch in s:
        if ch.isalpha():
            cur += 1
        else:
            if cur > 0:
                ans += 1
                cur = 0
    print(ans)