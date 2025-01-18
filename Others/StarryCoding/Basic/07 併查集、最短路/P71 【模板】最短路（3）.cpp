#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, q, u, v, w;
    cin >> n >> m >> q;
    vector<vector<int>> g(n, vector<int>(n, INF));
    for (int i = 0; i < n; ++i) g[i][i] = 0;
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        u--, v--;
        g[u][v] = min(g[u][v], w);
    }

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            if (k == i || g[i][k] == INF) continue;
            for (int j = 0; j < n; ++j) {
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }

    for (int i = 0; i < q; ++i) {
        cin >> u >> v;
        u--; v--;
        cout << (g[u][v] == INF ? -1 : g[u][v]) << endl;
    }
    return 0;
}