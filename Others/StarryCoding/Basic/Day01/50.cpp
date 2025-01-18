#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e3 + 5;
#define endl '\n'

LL a[N][N], d[N][N];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, m, q, x1, y1, x2, y2, c;
    cin >> n >> m >> q;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> a[i][j];
    for (int i = 1; i <= n; i++){ // 二維差分
        for (int j = 1; j <= m; j++) {
            d[i][j] += a[i][j];
            d[i + 1][j] -= a[i][j];
            d[i][j + 1] -= a[i][j];
            d[i + 1][j + 1] += a[i][j];
        }
    }
    while (q--) { // 區間修改
        cin >> x1 >> y1 >> x2 >> y2 >> c;
        d[x1][y1] += c;
        d[x2 + 1][y1] -= c;
        d[x1][y2 + 1] -= c;
        d[x2 + 1][y2 + 1] += c;
    }
    for (int i = 1; i <= n; i++) { // 還原
        for (int j = 1; j <= m; j++) {
            a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + d[i][j];
            cout << a[i][j] << " \n"[j == m];
        }
    }
    return 0;
}