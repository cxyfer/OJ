/*
P12212 [蓝桥杯 2023 国 Python B] 最大阶梯
https://www.luogu.com.cn/problem/P12212
*/

#include <bits/stdc++.h>
using namespace std;
const int COLORS = 11;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N; cin >> N;
    vector<vector<int>> grid(N, vector<int>(N));
    for (auto &row : grid) for (auto &x : row) cin >> x;

    int ans = 0;
    auto calc = [&]() -> void {
        vector<int> f(N, 0);
        for (int c = 0; c < COLORS; c++) {
            for (auto &row : grid) {
                for (int i = 0; i < N; i++) {
                    if (row[i] != c) f[i] = 0;
                    else f[i] = min((i > 0 ? f[i - 1] : 0), f[i]) + 1;
                }
                ans = max(ans, *max_element(f.begin(), f.end()));
            }
        }
    };

    // 旋轉 4 次
    for (int t = 0; t < 4; t++) {
        calc();
        // 旋轉 90 度（1. 轉置 2. 翻轉）
        for (int i = 0; i < N; i++)
            for (int j = 0; j < i; j++)
                swap(grid[i][j], grid[j][i]);
        for (auto &row : grid) reverse(row.begin(), row.end());
    }
    cout << ans << endl;
    return 0;
}