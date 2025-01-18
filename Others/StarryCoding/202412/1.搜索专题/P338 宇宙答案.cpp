#include <bits/stdc++.h>
using namespace std;
const int MAX_X = 2e6;
#define endl '\n'

int solve(int x, int y) {
    if (x == y) return 0;
    queue<pair<int, int>> q; // {x, dist}
    q.emplace(x, 0);
    vector<bool> vis(MAX_X + 1);
    while (!q.empty()) {
        auto [x, d] = q.front(); q.pop();
        if (x == y) return d;
        if (x < 0 || x > MAX_X || vis[x]) continue;
        vis[x] = true;
        q.emplace((int) (1.6 * x), d + 1);
        q.emplace((int) (0.6 * x), d + 1);
        q.emplace(x + 1, d + 1);
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, x, y;
    cin >> t;
    while (t--) {
        cin >> x >> y;
        cout << solve(x, y) << endl;
    }
    return 0;
}