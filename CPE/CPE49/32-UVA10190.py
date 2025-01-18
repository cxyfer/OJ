while True:
    try:
        m, n = map(int, input().split())
    except EOFError:
        break
    k = 0
    flag = True
    if m > 1 and n > 1:
        tmp = m
        while tmp % n == 0:
            k += 1
            tmp //= n
        if tmp != 1:
            flag = False
    else:
        flag = False
    if flag:
        for i in range(k, -1, -1):
            print(m, end=" " if i else "\n")
            m //= n
    else:
        print("Boring!")