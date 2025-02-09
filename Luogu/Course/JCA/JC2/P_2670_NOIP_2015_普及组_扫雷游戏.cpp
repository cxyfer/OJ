#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<string> mp(n);
    for (int i = 0; i < n; ++i) {
        cin >> mp[i];
    }

    vector<string> ans(n, string(m, '0'));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mp[i][j] == '*') {
                ans[i][j] = '*';
                continue;
            }
            for (int dx = -1; dx <= 1; ++dx) {
                for (int dy = -1; dy <= 1; ++dy) {
                    int x = i + dx, y = j + dy;
                    if (x >= 0 && x < n && y >= 0 && y < m && mp[x][y] == '*') ans[i][j]++;
                }
            }
        }
    }

    for (auto &row : ans) {
        cout << row << endl;
    }
    return 0;
}