#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
#define endl '\n'

int n, m;
vector<string> grid;
vector<vector<bool>> visited;

void dfs(int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m || grid[x][y] == '#' || visited[x][y]) return;
    visited[x][y] = true;
    for (int nx : {x + 1, x - 1}) dfs(nx, y);
    for (int ny : {y + 1, y - 1}) dfs(x, ny);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> n >> m;
    grid.resize(n);
    for (int i = 0; i < n; i++) cin >> grid[i];
    visited.assign(n, vector<bool>(m, false));
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '.' && !visited[i][j]) {
                dfs(i, j);
                ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}