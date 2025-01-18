N, A1, A2, A3 = map(int, input().split(" "))

ans = 0
for i in range(1, N//A1+1):
    for j in range(1, N//A2+1):
        for k in range(1, N//A3+1):
            # print(A1*i, A2*j, A3*k)
            if A1*i ^ A2*j ^ A3*k == 0:
                ans += 1
print(ans % 998244353)