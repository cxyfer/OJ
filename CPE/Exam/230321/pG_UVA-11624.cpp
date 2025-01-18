#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int DIR[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

class Node {
public:
    int x, y, time;
    bool is_fire;
    Node() {}
    Node (int x, int y, bool is_fire, int time) : x(x), y(y), is_fire(is_fire), time(time) {}
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, m;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        vector<string> grid(n);
        for (int i = 0; i < n; i++) {
            cin >> grid[i];
        }
        Node st;
        queue<Node> q; // (i, j, is_fire, time)
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '.') continue;
                if (grid[i][j] == 'F') {
                    q.push({i, j, true, 0});
                } else if (grid[i][j] == 'J') {
                    st = {i, j, false, 0};
                }
                vis[i][j] = true;
            }
        }
        q.push(st);
        int ans = -1;
        while (!q.empty()) {
            Node node = q.front(); q.pop();
            int x = node.x, y = node.y, time = node.time;
            bool is_fire = node.is_fire;
            if (!is_fire && (x == 0 || x == n - 1 || y == 0 || y == m - 1)) {
                ans = time + 1;
                break;
            }
            for (int k = 0; k < 4; k++) {
                int nx = x + DIR[k][0], ny = y + DIR[k][1];
                if (0 <= nx && nx < n && 0 <= ny && ny < m && !vis[nx][ny]) {
                    vis[nx][ny] = true;
                    q.push({nx, ny, is_fire, time + 1});
                }
            }
        }
        cout << (ans != -1 ? to_string(ans) : "IMPOSSIBLE") << endl;
    }
    return 0;
}