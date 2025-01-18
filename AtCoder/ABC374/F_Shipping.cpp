#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = LLONG_MAX / 2;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL N, K, X;
    cin >> N >> K >> X;
    vector<LL> T(N);
    for (int i = 0; i < N; i++) cin >> T[i];
    vector<LL> s(N + 1); // prefix sum
    for (int i = 0; i < N; i++) s[i + 1] = s[i] + T[i];

    // dfs(i, j) 表示考慮到前 i 個貨物(即已發送 i 個貨物)，且上一次發貨時間為 j 的最小總成本
    vector<unordered_map<LL, LL>> memo(N);
    function<LL(int, LL)> dfs = [&](int i, LL j) -> LL {
        if (i == N) return 0;
        if (memo[i].find(j) != memo[i].end()) return memo[i][j];
        LL &res = memo[i][j];
        res = LLONG_MAX / 2;
        // 枚舉這次發貨的貨物數量
        for (int k = 1; k <= min(K, N - i); k++) {
            // 這次發貨的時間，至少是上一次發貨的時間 + X 或 這批貨物的最晚發貨時間
            LL nxt_j = max(j + X, T[i + k - 1]);
            // sum_{T=i}^{i+k-1} (nxt_j - T_i)
            // = k * nxt_j - sum_{T=i}^{i+k-1} T_i = k * nxt_j - (s[i + k] - s[i])
            LL sum_T = s[i + k] - s[i];
            LL cur = k * nxt_j - sum_T + dfs(i + k, nxt_j);
            res = min(res, cur);
        }
        return res;
    };
    LL ans = dfs(0, -LLONG_MAX / 2);
    cout << ans << endl;
    return 0;
}