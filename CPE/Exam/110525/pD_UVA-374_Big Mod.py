kase = 1
while True:
    try:
        if kase > 1:
            input()
        B = int(input())
        P = int(input())
        M = int(input())
    except EOFError:
        break
    kase += 1
    # ans = pow(B, P, M) # python built-in pow is also exponentiating by squaring
    ans = 1
    while P:
        if P & 1:
            ans = ans * B % M
        B = B * B % M
        P >>= 1
    print(ans)