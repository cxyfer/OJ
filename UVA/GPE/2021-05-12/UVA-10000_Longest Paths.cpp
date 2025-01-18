#include <bits/stdc++.h>
using namespace std;
#define pii pair<int, int>
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, s, u, v, kase = 1;
    while (cin >> n && n) {
        cin >> s;
        vector<vector<int>> g(n + 1);
        while (cin >> u >> v && (u || v)) {
            g[u].push_back(v);
        }
        // Dijkstra
        vector<int> dist(n + 1, 0);
        priority_queue<pii, vector<pii>, greater<pii>> pq;
        pq.push({0, s});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d < dist[u]) continue;
            for (int v : g[u]) {
                int nd = d + 1;
                if (dist[v] < nd) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        // Find the longest path with smallest index
        int mx = 0, idx = s;
        for (int i = 1; i <= n; i++) {
            if (dist[i] > mx) mx = dist[i], idx = i;
        }
        cout << "Case " << kase++ << ": The longest path from " << s << " has length " << mx << ", finishing at " << idx << "." << endl << endl;
    }
    return 0;
}