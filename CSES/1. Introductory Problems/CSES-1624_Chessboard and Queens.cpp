/* CSES 1624: Chessboard and Queens
    Backtracking + Bitmask
*/
#include <bits/stdc++.h>
using namespace std;
const int N = 8;
#define endl '\n'

vector<string> mp(N);
vector<int> path(N); // row-i 的 Q 在 col-path[i]
int ans = 0;

bool check(int x, int y) {
    for (int i = 0; i < x; i++) {
        int j = path[i];
        if ((x+y) == (i+j) || (x-y) == (i-j)) return false; // 位在同一條斜線上 (斜率相同)
    }
    return true;
}

void dfs(int r, int avail) {
    if (r == N) {
        ans++;
        return;
    }
    for (int c = 0; c < N; c++) {
        if (avail & (1 << c) && mp[r][c] == '.' && check(r, c)) {
            path[r] = c;
            dfs(r+1, avail & ~(1 << c));
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    for (int i = 0; i < N; i++) cin >> mp[i];
    dfs(0, (1 << N) - 1);
    cout << ans << endl;
    return 0;
}