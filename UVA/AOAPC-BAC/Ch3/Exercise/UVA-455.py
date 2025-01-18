t = int(input())
for tc in range(t):
    input()
    s = input()
    n = len(s)

    for i in range(1, n + 1):
        if n % i == 0:
            if s[:i] * (n // i) == s:
                print(i)
                break
    if tc < t - 1:
        print()