M = int(input())

# 轉換為 3 進位制
ans = []
deg = 0
while M > 0:
    r = M % 3
    if r > 0:
        ans.extend([deg] * r)
    M = M // 3
    deg += 1

print(len(ans))
print(*ans)