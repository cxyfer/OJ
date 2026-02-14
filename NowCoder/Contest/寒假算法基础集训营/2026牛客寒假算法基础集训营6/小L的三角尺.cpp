#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
    int n, w;
    cin >> n >> w;
    vector<pair<double, double>> items(n);

    for (auto& [x, y] : items) cin >> x >> y;

    double ans = 0.0;
    priority_queue<pair<double, int>> pq;
    for (int i = 0; i < n; i++) {
        auto [x, y] = items[i];
        ans += hypot(x, y);
        if (y > 0) pq.push({hypot(x, y) - hypot(x, y - 1), i});
    }

    while (w-- > 0 && !pq.empty()) {
        auto [v, i] = pq.top(); pq.pop();
        ans -= v;
        items[i].second--;
        if (items[i].second > 0) {
            auto [x, y] = items[i];
            pq.push({hypot(x, y) - hypot(x, y - 1), i});
        }
    }
    cout << fixed << setprecision(10) << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}