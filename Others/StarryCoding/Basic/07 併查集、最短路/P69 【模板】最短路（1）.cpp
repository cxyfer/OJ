#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define PII pair<int, int>
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v, w;
    cin >> n >> m;
    vector<vector<PII>> g(n);
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        u--; v--;
        g[u].push_back({v, w});
    }

    vector<int> dist(n, INF);
    dist[0] = 0;
    priority_queue<PII, vector<PII>, greater<>> pq;
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : g[u]) {
            int nd = dist[u] + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                pq.push({nd, v});
            }
        }
    }
    cout << (dist[n - 1] == INF ? -1 : dist[n - 1])<< endl;
    return 0;
}