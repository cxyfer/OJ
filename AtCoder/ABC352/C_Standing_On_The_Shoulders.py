N = int(input())
ans = s = 0
for i in range(N):
    a, b = map(int, input().split())
    s += a
    ans = max(ans, b-a) # 最大的頭部高度
print(s+ans) # 頭部高度 + 總身高