#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n; cin >> n;
    vector<int> fa(n, -1);
    vector<vector<int>> g(n);
    for (int i = 1; i < n; ++i) {
        cin >> fa[i];
        fa[i]--;
        g[fa[i]].push_back(i);
    }

    vector<int> ans(n, 0);
    auto dfs = [&](auto &&dfs, int u) -> void {
        for (int v : g[u]) {
            dfs(dfs, v);
            ans[u] += ans[v] + 1;
        }
    };
    dfs(dfs, 0);

    for (int i = 0; i < n; ++i) cout << ans[i] << " \n"[i == n - 1];
    return 0;
}