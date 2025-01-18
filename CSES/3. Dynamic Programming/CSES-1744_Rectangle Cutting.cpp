#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int a, b;
    cin >> a >> b;
    // dp[x][y] 表示將 x * y 的矩形切成所有正方形的最小切割次數
    vector<vector<int>> f(a + 1, vector<int>(b + 1, INF));
    for (int i = 1; i <= min(a, b); i++) { // 正方形不用切割
        f[i][i] = 0;
    }
    for (int i = 1; i <= a; i++) {
        for (int j = 1; j <= b; j++) {
            for (int k = 1; k < i; k++) { // 枚舉橫切點
                f[i][j] = min(f[i][j], f[k][j] + f[i - k][j] + 1);
            }
            for (int k = 1; k < j; k++) { // 枚舉縱切點
                f[i][j] = min(f[i][j], f[i][k] + f[i][j - k] + 1);
            }
        }
    }
    cout << f[a][b] << endl;
    return 0;
}