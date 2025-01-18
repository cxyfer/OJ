T = int(input())

for _ in range(1, T+1):
    n, m = map(int, input().split())
    words = [input() for _ in range(m)]

    ans = n * m
    for i in range(m-1):
        wa, wb = words[i], words[i+1]
        for i in range(n):
            if wa[i:] == wb[:n-i]:
                ans -= n - i
                break
    print(ans)