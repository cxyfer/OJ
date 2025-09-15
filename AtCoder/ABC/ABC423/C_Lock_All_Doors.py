def solve():
    N, R = map(int, input().split())
    L = list(map(int, input().split()))
    flag = True
    pre1 = suf1 = 0
    cnt1 = cnt2 = 0
    for i in range(R):
        if L[i] == 1:
            if flag:
                pre1 += 1
            else:
                cnt1 += 1
        else:
            flag = False
    flag = True
    for i in range(N - 1, R - 1, -1):
        if L[i] == 1:
            if flag:
                suf1 += 1
            else:
                cnt2 += 1
        else:
            flag = False
    print(N - (pre1 + suf1) + cnt1 + cnt2)

if __name__ == "__main__":
    solve()