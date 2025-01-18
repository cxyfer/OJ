"""
包含 A[i] 的子陣列左端點有 i+1 個，右端點有 n-i 個
所以包含 A[i] 的子陣列有 (i+1)*(n-i) 個

因此 A[i] 被 XOR 了 (i+1)*(n-i) 次
如果 (i+1)*(n-i) 是奇數，則 A[i] 對答案有貢獻

但有更強的性質：
- 如果 n 是偶數，則 (i+1)*(n-i) 也必定是偶數，因此答案必定是 0
- 如果 n 是奇數，則
    - 當 i 是偶數時，(i+1)*(n-i) 是奇數
    - 當 i 是奇數時，(i+1)*(n-i) 是偶數
因此，答案就是所有偶數下標的 XOR
"""
n = int(input())
A = list(map(int, input().split()))

# ans = 0
# for i in range(n):
#     if (i + 1) * (n - i) & 1:
#         ans ^= A[i]
# print(ans)
if n & 1:
    ans = 0
    for i in range(0, n, 2):
        ans ^= A[i]
    print(ans)
else:
    print(0)