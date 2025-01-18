"""
    CPE49
"""
while True:
    try:
        m, n = map(int, input().split())
    except EOFError:
        break
    flag = True if m > 1 and n > 1 else False # (1, n) or (m, 1) is boring
    if flag:
        ans = [m]
        while m % n == 0:
            m //= n
            ans.append(m)
        flag = True if m == 1 else False
    if flag:
        print(*ans)
    else:
        print("Boring!")