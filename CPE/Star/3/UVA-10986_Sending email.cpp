#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int T, kase = 1, n, m, s, t;
    cin >> T;
    while (T--) {
        cin >> n >> m >> s >> t;
        vector<vector<pair<int, int>>> g(n);
        for (int i = 0; i < m; ++i) {
            int u, v, w;
            cin >> u >> v >> w;
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }
        vector<int> dist(n, INT_MAX);
        dist[s] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, s});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d > dist[u]) continue;
            for (auto [v, w] : g[u]) {
                int nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        cout << "Case #" << kase++ << ": " << (dist[t] == INT_MAX ? "unreachable" : to_string(dist[t])) << endl;
    }
    return 0;
}