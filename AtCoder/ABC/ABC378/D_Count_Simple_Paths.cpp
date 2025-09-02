#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    vector<pair<int, int>> DIR = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int H, W, K; cin >> H >> W >> K;
    vector<string> grid(H);
    for (int i = 0; i < H; i++) {
        cin >> grid[i];
    }
    int ans = 0;
    auto dfs = [&](auto &&dfs, int x, int y, int step) -> void {
        if (step == K) {
            ans += 1;
            return;
        }
        for (auto [dx, dy] : DIR) {
            int nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < H && ny >= 0 && ny < W && grid[nx][ny] == '.') {
                grid[nx][ny] = '#';
                dfs(dfs, nx, ny, step + 1);
                grid[nx][ny] = '.';
            }
        }
    };
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (grid[i][j] == '.') {
                grid[i][j] = '#';
                dfs(dfs, i, j, 0);
                grid[i][j] = '.';
            }
        }
    }
    cout << ans << endl;
    return 0;
}