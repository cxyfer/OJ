#include <bits/stdc++.h>
using namespace std;
using LL = long long;
using PLL = pair<LL, LL>;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, k, u, v, w;
    cin >> n >> m >> k;
    vector<vector<PLL>> g(n);
    for (int i = 0; i < m; i++) {
        cin >> u >> v >> w;
        g[u - 1].push_back({v - 1, w});
    }

    vector<LL> cnt(n, 0);
    vector<LL> ans;
    priority_queue<PLL, vector<PLL>, greater<PLL>> pq; // Min-Heap
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (u == n - 1 && cnt[u] >= k) break;
        if (cnt[u] >= k) continue;
        cnt[u]++;
        if (u == n - 1) ans.push_back(d);
        for (auto [v, w] : g[u]) {
            pq.push({d + w, v});
        }
    }

    for (int i = 0; i < k; i++) {
        cout << ans[i] << " \n"[i == k - 1];
    }
    return 0;
}