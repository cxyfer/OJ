while True:
    try:
        n = int(input())
    except EOFError:
        break

    ans = 0
    while n >= 3:
        ans += n // 3 * 3
        n = n // 3 + n % 3
    if n == 2: # 剩下2個的時候，可以借1個，變成3個
        ans += 3
    else: # 否則無法借，只能自己喝掉
        ans += n
    print(ans)