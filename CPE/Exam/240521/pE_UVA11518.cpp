#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

vector<vector<int>> g;
vector<bool> visited;

int dfs(int u) {
    visited[u] = true;
    int res = 1;
    for (int v : g[u]) {
        if (!visited[v]) {
            res += dfs(v);
        }
    }
    return res;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, m, l, u, v, z;
    cin >> t;
    while (t--) {
        cin >> n >> m >> l;
        g.clear();
        g.resize(n);
        for (int i=0; i<m; i++) {
            cin >> u >> v;
            g[u-1].push_back(v-1);
        }
        int ans = 0;
        visited.assign(n, false);
        for (int i=0; i<l; i++) {
            cin >> z;
            if (!visited[z-1]) {
                ans += dfs(z-1);
            }
        }
        cout << ans << endl;
    }
    return 0;
}