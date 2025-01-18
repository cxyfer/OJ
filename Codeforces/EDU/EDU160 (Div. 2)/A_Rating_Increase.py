T = int(input())

for tc in range(1, T+1):
    s = input()
    n = len(s)
    ans = []
    for i in range(1, n):
        if int(s[:i]) < int(s[i:]) and s[i] != '0':
            ans = [s[:i], s[i:]]
            break
    print(*ans) if ans else print('-1')