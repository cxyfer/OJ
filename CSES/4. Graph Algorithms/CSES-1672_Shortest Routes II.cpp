#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 1e18;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL n, m, q, u, v, w;
    cin >> n >> m >> q;
    vector<vector<LL>> g(n, vector<LL>(n, INF));
    for (int i = 0; i < n; i++) g[i][i] = 0;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        u--, v--;
        g[u][v] = min(g[u][v], w);
        g[v][u] = min(g[v][u], w);
    }

    // Floyd-Warshall
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            if (i == k || g[i][k] == INF) continue;
            for (int j = 0; j < n; j++) {
                if (j == k || g[k][j] == INF) continue;
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }

    while (q--) {
        cin >> u >> v;
        u--, v--;
        cout << (g[u][v] == INF ? -1 : g[u][v]) << endl;
    }
    return 0;
}