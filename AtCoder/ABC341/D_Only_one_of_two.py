import math

N, M, K = map(int, input().split())

lcm = math.lcm(N, M)

n = lcm // N + lcm // M - 2 # 每lcm個數字中，有N個是A的倍數，有M個是B的倍數，但是有一個lcm既是A的倍數又是B的倍數，所以要減2

if K % n == 0:
    ans = lcm * (K // n) - min(N, M)
else:
    ans = lcm * (K // n)
    k = K % n
    i, j = 1, 1
    flag = 0
    while k > 0:
        if i * N < j * M:
            i += 1
            k -= 1
            flag = 0
        else:
            j += 1
            k -= 1
            flag = 1
    ans += (i-1) * N if flag == 0 else (j-1) * M

print(ans)