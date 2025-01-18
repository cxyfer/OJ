"""
    貢獻法 + 乘法原理
    包含 A[i] 的子陣列左端點有 i+1 個，右端點有 n-i 個
    所以包含 A[i] 的子陣列有 (i+1)*(n-i) 個
"""
n = int(input())
A = list(map(int, input().split()))

ans = 0
for i, x in enumerate(A):
    ans += x * (i + 1) * (n - i)
print(ans)