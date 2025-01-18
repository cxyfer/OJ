#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define PII pair<int, int>

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<string> grid(n);
    for (int i = 0; i < n; i++) cin >> grid[i];

    PII st, ed;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'A') st = {i, j};
            else if (grid[i][j] == 'B') ed = {i, j};
        }
    }

    vector<PII> DIR = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    vector<char> DIRCH = {'D', 'U', 'R', 'L'};
    vector<vector<bool>> vis(n, vector<bool>(m, false));
    vector<vector<char>> dir(n, vector<char>(m, ' '));
    vector<vector<PII>> pre(n, vector<PII>(m, {-1, -1}));

    queue<PII> q;
    q.push(st);
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        if (x == ed.first && y == ed.second) {
            string ans;
            while (x != st.first || y != st.second) {
                ans += dir[x][y];
                auto [px, py] = pre[x][y];
                x = px;
                y = py;
            }
            cout << "YES" << endl;
            reverse(ans.begin(), ans.end());
            cout << ans.size() << endl;
            cout << ans << endl;
            return 0;
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + DIR[i].first;
            int ny = y + DIR[i].second; 
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || grid[nx][ny] == '#' || vis[nx][ny]) continue;
            vis[nx][ny] = true;
            dir[nx][ny] = DIRCH[i];
            pre[nx][ny] = {x, y};
            q.push({nx, ny});
        }
    }
    cout << "NO" << endl;
    return 0;
}