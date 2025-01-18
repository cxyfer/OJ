t = int(input())

for _ in range(t):
    N = int(input())
    S = list(input())
    ans = 0
    i = 0
    while i < N:
        if S[i] == '*':
            if (i + 1) < N and S[i + 1] == '*':
                break
            else:
                i += 1
        else:
            if S[i] == '@':
                ans += 1
            i += 1
    print(ans)