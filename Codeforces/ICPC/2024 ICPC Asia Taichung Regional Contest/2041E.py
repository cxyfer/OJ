a, b = map(int, input().split())
if a == b:
    print(f"1\n{a}")
else:
    print(5)
    print(*[b, b, b, b, 5 * a - 4 * b])