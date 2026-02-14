#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
using ti3 = tuple<int, int, int>;
#define endl '\n'

const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

void solve() {
    int n, m, a, b;
    cin >> n >> m >> a >> b;

    priority_queue<ti3, vector<ti3>, greater<ti3>> pq;
    vector<vector<int>> dist(n, vector<int>(m, INF));
    vector<vector<int>> avail(n, vector<int>(m, 0));

    int r, c, t;
    for (int i = 0; i < a; i++) {
        cin >> r >> c;
        r--, c--;
        dist[r][c] = 0;
        pq.emplace(0, r, c);
    }
    for (int i = 0; i < b; i++) {
        cin >> r >> c >> t;
        r--, c--;
        avail[r][c] = t;
    }

    int ans = 0;
    while (!pq.empty()) {
        auto [d, r, c] = pq.top(); pq.pop();
        if (d > dist[r][c]) continue;
        ans = max(ans, d);
        for (auto [dr, dc] : dirs) {
            int nr = r + dr, nc = c + dc;
            if (0 <= nr && nr < n && 0 <= nc && nc < m) {
                int nd = max(d + 1, avail[nr][nc]);
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    pq.push({nd, nr, nc});
                }
            }
        }
    }
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}