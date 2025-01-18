def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        n = int(input())
    except EOFError:
        break
    m = int(str(n)[::-1])
    ck1 = is_prime(n)
    ck2 = is_prime(m)
    if ck1 and ck2 and n != m:
        print(f"{n} is emirp.")
    elif ck1:
        print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")
