#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e7 + 10;
const int INF = 0x3f3f3f3f;
#define endl '\n'

LL dp[N];
LL dfs(LL n){
    if (n == 1) return 1;
    if (n < N && dp[n] != -1) return dp[n];
    LL res = 0;
    if (n & 1) res = dfs(3*n+1) + 1;
    else res = dfs(n/2) + 1;
    if (n < N) dp[n] = res;
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL a, b, ans;
    memset(dp, -1, sizeof(dp));
    while (cin >> a >> b) {
        ans = -INF;
        for (int i = min(a, b); i <= max(a, b); i++){
            ans = max(ans, dfs(i));
        }
        cout << a << " " << b << " " << ans << endl;
    }
    return 0;
}