#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 1e18;
#define endl '\n'

struct Edge {
    int st, ed, w;
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].st >> edges[i].ed >> edges[i].w;
        edges[i].st--, edges[i].ed--;
    }

    // Bellman-Ford
    // 1. 更新最長路徑
    vector<LL> dist(n, -INF);
    dist[0] = 0;
    for (int i = 0; i < n; i++) {
        for (const auto& e : edges) {
            if (dist[e.st] != -INF) {
                dist[e.ed] = max(dist[e.ed], dist[e.st] + e.w);
            }
        }
    }
    
    // 2. 檢查是否存在正環
    for (int i = 0; i < n; i++) {
        for (const auto& e : edges) {
            // if (dist[e.st] == INF) {
            //     dist[e.ed] = INF;
            //     continue;
            // }

            // 還能被 relax ，代表存在「正環」（因為取 max）
            if (dist[e.st] != -INF && dist[e.st] + e.w > dist[e.ed]) {
                dist[e.ed] = INF;
            }
        }
    }

    cout << (dist[n - 1] != INF ? dist[n - 1] : -1) << endl;
    return 0;
}