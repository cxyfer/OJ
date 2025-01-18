while True:
    try:
        n = input()
    except EOFError:
        break
    a, b, c = map(int, list(n))
    if int(n) == a ** 3 + b ** 3 + c ** 3:
        print('Yes')
    else:
        print('No')