/*
分別從起點和終點跑一次 Dijkstra，之後枚舉要在哪條邊上使用折價券
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 1e18;
#define endl '\n'

struct Edge {
    int st, ed, w;
};

struct Node {
    int u;
    LL d;
    bool operator>(const Node& other) const {
        return d > other.d;
    }
};

vector<LL> dijkstra(const vector<vector<pair<int, int>>>& g, int st) {
    vector<LL> dist(g.size(), INF);
    dist[st] = 0;
    priority_queue<Node, vector<Node>, greater<Node>> pq; // min heap
    pq.push({st, 0});
    while (!pq.empty()) {
        auto [u, d] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto& [v, w] : g[u]) {
            LL nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                pq.push({v, nd});
            }
        }
    }
    return dist;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<Edge> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].st >> edges[i].ed >> edges[i].w;
        edges[i].st--, edges[i].ed--;
    }

    vector<vector<pair<int, int>>> g1(n), g2(n);
    for (const auto& e : edges) {
        g1[e.st].emplace_back(e.ed, e.w);
        g2[e.ed].emplace_back(e.st, e.w);
    }

    auto dist1 = dijkstra(g1, 0);
    auto dist2 = dijkstra(g2, n - 1);

    // 枚舉要在哪條邊上使用折價券
    LL ans = INF;
    for (const auto& e : edges) {
        ans = min(ans, dist1[e.st] + e.w / 2 + dist2[e.ed]);
    }
    cout << ans << endl;
    return 0;
}