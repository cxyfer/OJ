while True:
    n = int(input())
    if n == 0:
        break

    while n > 9:
        t = 0
        while n > 0:
            t += n % 10
            n //= 10
        n = t
    print(n)