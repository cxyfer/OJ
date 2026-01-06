"""
U360487 灵茶八题 - 子数组 ^w^
https://www.luogu.com.cn/problem/U360487

和 +w+ 相同，包含 A[i] 的子陣列左端點有 i+1 個，右端點有 n-i 個
所以包含 A[i] 的子陣列有 (i+1)*(n-i) 個

因此 A[i] 被 XOR 了 (i+1)*(n-i) 次
如果 (i+1)*(n-i) 是奇數，則 A[i] 對答案有貢獻
可在 O(n) 時間內計算

但可以繼續討論：
- 如果 n 是偶數，則 (i+1)*(n-i) 也必定是偶數，因此答案必定是 0
- 如果 n 是奇數，則
    - 當 i 是偶數時，(i+1)*(n-i) 是奇數，A[i] 對答案有貢獻
    - 當 i 是奇數時，(i+1)*(n-i) 是偶數，A[i] 對答案沒有貢獻
因此，答案就是所有偶數下標的 XOR
可在 O(1) 時間內計算
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