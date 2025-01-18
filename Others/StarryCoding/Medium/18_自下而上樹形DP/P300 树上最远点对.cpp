#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, f, w;
    cin >> n;
    vector<vector<pair<int, int>>> g(n + 1);
    for (int i = 2; i <= n; i++) {
        cin >> f >> w;
        g[f].push_back({i, w});
        g[i].push_back({f, w});
    }
    LL ans = 0;
    auto dfs = [&](auto &&dfs, int u, int fa) -> LL {
        LL first = 0, second = 0;
        for (auto [v, w] : g[u]) {
            if (v == fa) continue;
            LL d = dfs(dfs, v, u) + w;
            if (d > first) {
                second = first;
                first = d;
            } else if (d > second) {
                second = d;
            }
        }
        ans = max(ans, first + second);
        return first;
    };
    dfs(dfs, 1, 0);
    cout << ans << endl;
    return 0;
}