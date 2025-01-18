#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

struct Node {
    int x, y, step;
};

const vector<int> dx = {0, 1, 0, -1};
const vector<int> dy = {1, 0, -1, 0};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> grid[i][j];

    vector<vector<bool>> vis(n, vector<bool>(m));
    queue<Node> q;
    q.push({0, 0, 0});
    vis[0][0] = true;
    while (!q.empty()) {
        auto [x, y, step] = q.front(); q.pop();
        if (x == n - 1 && y == m - 1) {
            cout << step << endl;
            return 0;
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || vis[nx][ny] || grid[nx][ny] == 1) continue;
            q.push({nx, ny, step + 1});
            vis[nx][ny] = true;
        }
    }
    cout << -1 << endl;
    return 0;
}