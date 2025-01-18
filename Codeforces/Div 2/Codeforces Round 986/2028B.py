t = int(input())

for _ in range(t):
    n, b, c = map(int, input().split())
    if b == 0:
        if n == 1:
            ans = 0 if c == 0 else 1
        else:
            ans = -1 if c == 0 else n - 1
    else:
        if b == 1 and c == 0:
            ans = 0
        else:
            if c > n - 1:
                m = 0
            else:
                m = (n - 1 - c) // b + 1
                if c + (m - 1) * b > n - 1:
                    m -= 1
            ans = n - m
    print(ans)