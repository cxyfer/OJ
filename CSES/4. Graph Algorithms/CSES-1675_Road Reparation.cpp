#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

struct Node {
    int v, w;
    bool operator>(const Node &other) const {
        return w > other.w;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, u, v, w;
    cin >> n >> m;
    vector<vector<Node>> g(n);
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        u--, v--;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }

    priority_queue<Node, vector<Node>, greater<Node>> pq;
    vector<bool> selected(n);
    selected[0] = true;
    for (auto [v, w] : g[0]) pq.push({v, w});

    LL ans = 0, cnt = 1;
    while (!pq.empty() && cnt < n) {
        auto [u, w] = pq.top(); pq.pop();
        if (selected[u]) continue;
        selected[u] = true;
        ans += w;
        cnt++;
        for (auto [v, w] : g[u]) {
            if (selected[v]) continue;
            pq.push({v, w});
        }
    }
    cout << (cnt == n ? to_string(ans) : "IMPOSSIBLE") << endl;
    return 0;
}