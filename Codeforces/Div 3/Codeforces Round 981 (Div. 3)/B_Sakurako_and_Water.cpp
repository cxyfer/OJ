/*
    貪心
    注意到增加高度是沒有副作用的，因此每次需要增加時，都可以盡可能的使用最大範圍。
    而每次增加的位置為對角線，因此可以維護該對角線的增加次數。
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<vector<int>> M(n, vector<int>(n));
        for (auto &row : M) {
            for (auto &val : row) cin >> val;
        }
        vector<int> d(2 * n + 1); // 對角線，做了偏移
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int c = i - j + n;
                if (M[i][j] + d[c] < 0) d[c] = -M[i][j]; // 還需要增加
            }
        }
        cout << accumulate(d.begin(), d.end(), 0) << endl;
    }
    return 0;
}