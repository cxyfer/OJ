#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

vector<int> DX = {-1, 0, 1};
int n, m;
vector<vector<int>> grid, memo, nxt;

int dfs(int x, int y) {
    if (y == m - 1) return grid[x][y];
    int &res = memo[x][y];
    if (res != INF) return res;
    for (int dx : DX) {
        int nx = (x + dx + n) % n; // 環狀處理
        int nd = dfs(nx, y + 1) + grid[x][y];
        if (nd < res || (nd == res && nx < nxt[x][y])) {
            res = nd;
            nxt[x][y] = nx; // 記錄下一個 column 是哪一個 row
        }
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    while (cin >> n >> m) {
        grid.assign(n, vector<int>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        // dfs(x, y) 表示從 (x, y) 到最後一個 column 的最短路徑
        memo.assign(n, vector<int>(m, INF));
        nxt.assign(n, vector<int>(m, -1)); // 紀錄路徑

        // 求從第一個 column 的任意位置到最後一個 column 的最短路徑
        int ans = INF, idx = 0;
        for (int i = 0; i < n; i++) {
            int res = dfs(i, 0);
            if (res < ans) ans = res, idx = i;
        }
        // 輸出路徑
        for (int y = 0; y < m; y++) {
            cout << idx + 1 << (y == m - 1 ? '\n' : ' ');
            idx = nxt[idx][y];
        }
        cout << ans << endl;
    }
    return 0;
}