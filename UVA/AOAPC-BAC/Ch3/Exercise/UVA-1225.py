t = int(input())

for _ in range(t):
    n = int(input())
    ans = [0] * 10
    for x in range(1, n + 1):
        tmp = x
        while tmp:
            ans[tmp % 10] += 1
            tmp //= 10
    print(" ".join(map(str, ans)))