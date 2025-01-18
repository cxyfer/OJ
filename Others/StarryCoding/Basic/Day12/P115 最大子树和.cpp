#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 0x3f3f3f3f3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, u, v;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> W(n);
        for (int i = 0; i < n; i++) cin >> W[i];
        vector<vector<int>> g(n);
        for (int i = 1; i < n; i++) {
            cin >> u >> v;
            g[u - 1].push_back(v - 1);
            g[v - 1].push_back(u - 1);
        }
        LL ans = -INF;
        vector<int> memo(n);
        function<int(int, int)> dfs = [&](int u, int fa) {
            LL res = W[u];
            for (auto v : g[u]) {
                if (v == fa) continue;
                res += max(0, dfs(v, u));
            }
            ans = max(ans, res);
            return res;
        };
        dfs(0, -1);
        cout << ans << endl;
    }
    return 0;
}