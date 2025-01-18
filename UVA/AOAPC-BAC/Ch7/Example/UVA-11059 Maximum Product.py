kase = 1
while True:
    try:
        n = int(input().strip())
        A = list(map(int, input().strip().split()))
    except EOFError:
        break
    try:
        input()
    except EOFError:
        pass
    ans = 0
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j + 1):
                prod *= A[k]
            ans = max(ans, prod)
    print(f"Case #{kase}: The maximum product is {ans}.")
    print()
    kase += 1
