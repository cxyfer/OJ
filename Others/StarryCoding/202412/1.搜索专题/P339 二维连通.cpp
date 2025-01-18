#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, m, k;
    vector<int> dx = {0, 0, 1, -1}, dy = {1, -1, 0, 0};
    cin >> t;
    while (t--) {
        cin >> n >> m >> k;
        vector<vector<int>> A(n, vector<int>(m));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> A[i][j];
        
        // DFS 找連通分量大小
        vector<vector<bool>> vis(n, vector<bool>(m));
        auto dfs = [&](auto &&dfs, int x, int y) -> int {
            if (vis[x][y]) return 0;
            vis[x][y] = true;
            int res = 1;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || A[nx][ny] == 1) continue;
                res += dfs(dfs, nx, ny);
            }
            return res;
        };

        // 找到每個連通分量
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (A[i][j] == 1 || vis[i][j]) continue;
                int res = dfs(dfs, i, j);
                if (res >= k) ans.push_back(res);
            }
        }

        // 輸出
        if (ans.size() == 0) {
            cout << -1 << endl;
        }
        else {
            sort(ans.begin(), ans.end());
            for (int i = 0; i < ans.size(); i++) {
                cout << ans[i] << (i == ans.size() - 1 ? endl : ' ');
            }
        }
    }
    return 0;
}