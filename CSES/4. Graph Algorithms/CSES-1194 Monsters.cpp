#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Node {
    int x, y, flag;
};

struct Info {
    int x, y;
    char dir;
    Info(int x, int y, char dir) : x(x), y(y), dir(dir) {}
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<string> grid(n);
    for (int i = 0; i < n; i++) cin >> grid[i];

    vector<Info> DIR = {{0, 1, 'R'}, {0, -1, 'L'}, {1, 0, 'D'}, {-1, 0, 'U'}};
    queue<Node> q;
    Node st;
    vector<vector<bool>> vis(n, vector<bool>(m, false));
    vector<vector<Info>> pre(n, vector<Info>(m, {-1, -1, ' '}));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '.') continue;
            if (grid[i][j] == 'A') st = {i, j, 0};
            else if (grid[i][j] == 'M') q.push({i, j, 1});
            vis[i][j] = true;
        }
    }

    q.push(st);
    while (!q.empty()) {
        auto [x, y, flag] = q.front(); q.pop();

        if (flag == 0 && (x == 0 || x == n - 1 || y == 0 || y == m - 1)) {
            cout << "YES" << endl;
            string ans;
            while (x != -1 && y != -1 && pre[x][y].dir != ' ') {
                ans += pre[x][y].dir;
                auto [nx, ny, dir] = pre[x][y];
                x = nx, y = ny;
            }
            reverse(ans.begin(), ans.end());
            cout << ans.size() << endl;
            cout << ans << endl;
            return 0;
        }

        for (auto [dx, dy, dir] : DIR) {
            int nx = x + dx, ny = y + dy;
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || vis[nx][ny]) continue;
            vis[nx][ny] = true;
            pre[nx][ny] = {x, y, dir};
            q.push({nx, ny, flag});
        }
    }
    cout << "NO" << endl;
    return 0;
}