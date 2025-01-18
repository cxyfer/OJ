n, a, b = map(int, input().split())

if 0 <= a - b <= n and 0 <= a + b <= n:
    if b != 0:
        print(a - b, a + b)
    else:
        print(a)
elif 0 <= a - b <= n:
    print(a - b)
elif 0 <= a + b <= n:
    print(a + b)
else:
    print("No solution")