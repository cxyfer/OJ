#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

vector<vector<char>> solve(long long K) {
    const int B = bit_width(static_cast<unsigned long long>(K));
    const int n = 3 * B + 1;
    vector<vector<char>> grid(n, vector<char>(n, '#'));

    grid[0][0] = '.';
    grid[n - 1][n - 1] = '.';
    for (int i = 0; i < n; i++) grid[i][n - 1] = '.';

    for (int b = 0; b < B; b++) {
        int r = 3 * b, c = b;
        for (int i = r; i <= r + 3; i++) grid[i][c] = '.';
        for (int i = r + 2; i <= r + 3; i++) grid[i][c + 1] = '.';

        if ((K >> b) & 1LL) {
            for (int j = c; j < n; j++) grid[r][j] = '.';
        } 
    }
    return grid;
}

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);
//     long long K;
//     cin >> K;
//     auto ans = solve(K);
//     cout << ans.size() << ' ' << ans[0].size() << endl;
//     for (auto& row : ans) {
//         for (char ch : row) cout << ch;
//         cout << endl;
//     }
//     return 0;
// }