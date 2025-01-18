#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> W(n);
    for (int i = 0; i < n; i++) cin >> W[i];
    vector<vector<int>> g(n);
    vector<int> indeg(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        u--, v--;
        g[v].push_back(u);
        indeg[u] += 1;
    }
    int root = 0;
    for (int i = 0; i < n; i++) {
        if (indeg[i] == 0) {
            root = i;
            break;
        }
    }
    auto dfs = [&](auto &&dfs, int u, int fa) -> pair<LL, LL> {
        LL f0 = 0, f1 = W[u]; // 不選 u / 選 u
        for (auto v : g[u]) {
            if (v == fa) continue;
            auto [g0, g1] = dfs(dfs, v, u);
            f0 += max(g0, g1); // 不選 u 的時候，v 可以選也可以不選
            f1 += g0; // 選 u 的時候，v 只能不選
        }
        return {f0, f1};
    };
    auto [f0, f1] = dfs(dfs, root, -1);
    cout << max(f0, f1) << endl;
    return 0;
}