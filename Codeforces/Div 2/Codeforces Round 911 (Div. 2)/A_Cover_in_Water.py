T = int(input())

for tc in range(1, T+1):
    N = int(input())
    S = input()

    ans = 0
    tmp = 0 # 連續空格的數目

    for ch in S:
        if ch == '.':
            tmp += 1
            if tmp == 3:
                ans = 2
                break
            ans += 1
        else:
            tmp = 0
    print(ans)