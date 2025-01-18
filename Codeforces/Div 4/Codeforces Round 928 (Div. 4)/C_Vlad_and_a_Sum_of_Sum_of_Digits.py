t = int(input())

ans = [0] * (2* 10**5+1)
ans[1] = 1
for i in range(2* 10**5+1):
    ans[i] = ans[i-1] + sum(map(int, list(str(i))))

for _ in range(t):
    N = int(input())
    print(ans[N])
    
    # b = 0
    # while N > 0:
    #     x, y = N // 10, N % 10
        
    #     s += 45 * (x) * (10**b)
    #     s += (1 + y) * y // 2 + b * (y+1)
    #     N = N // 10
    #     b += 1
    #     print(f"x: {x}, y: {y}, s: {s}, b: {b}")
    # s += N
    # print(s)

# def digitSum(n):
#     return sum(map(int, list(str(n))))
# for _ in range(t):
#     N = int(input())
#     s = 0
#     for i in range(1, N+1):
#         s += digitSum(i)
#     print(s)