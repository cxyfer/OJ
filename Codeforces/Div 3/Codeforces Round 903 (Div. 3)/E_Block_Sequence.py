from functools import lru_cache

t = int(input())

@lru_cache(None)
def solve(i, j):
    n = j - i + 1
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    ans = n
    for idx in range(i, j+1):
        if A[idx] <= (n-1)-idx:
            ans = min(ans, idx + solve(idx+A[idx]+1, j))
            if ans <= idx:
                return ans
    # for idx, num in enumerate(nums):
    #     if num <= (n-1)-idx:
    #         # print(idx, num)

    #         ans = min(ans, idx + solve(nums[idx+num+1:]))
    #         if ans <= idx:
    #             return ans
    return ans
for case in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    # print("Case #{}: ".format(case+1))
    dp = [float('inf') for _ in range(N+1)]
    dp[0] = 0
    for i in range(1, N+1):
        dp[i] = min(dp[i], dp[i-1]+1)
        j = min(i+A[i]+1, N+1)
        dp[j] = min(dp[j], dp[i])
        j = min(i+A[i]+1, N+1)
        dp[j] = min(dp[j], dp[i])
    print(ans)
# void solve() {
#     int n;
#     cin >> n;
#     for(int i = 1; i <= n; i ++ ) cin >> a[i], f[i] = INF;
#     f[1] = 0;
#     f[n + 1] = INF;
#     for(int i = 1; i <= n; i ++ ) {
#         f[i + 1] = min(f[i + 1], f[i] + 1);
#         int j = min(i + a[i] + 1, n + 2);
#         f[j] = min(f[j], f[i]);
#     }
#     cout << f[n + 1] << '\n';
}