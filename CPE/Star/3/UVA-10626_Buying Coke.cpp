#include <bits/stdc++.h>
using namespace std;
const int A = 705, B = 205, C = 55;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int memo[A][B][C];

int dfs(int k, int a, int b, int c) {
    if (k == 0) return 0;
    int &res = memo[a][b][c];
    if (res != INF) return res;
    if (a >= 8) res = min(res, dfs(k - 1, a - 8, b, c) + 8);
    if (a >= 3 && b >= 1) res = min(res, dfs(k - 1, a - 3, b - 1, c) + 4);
    if (b >= 2) res = min(res, dfs(k - 1, a + 2, b - 2, c) + 2);
    if (c >= 1) res = min(res, dfs(k - 1, a + 2, b, c - 1) + 1);
    if (a >= 3 && c >= 1) res = min(res, dfs(k - 1, a - 3, b + 1, c - 1) + 4);
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, k, a, b, c;
    cin >> t;
    while (t--) {
        cin >> k >> a >> b >> c;
        memset(memo, INF, sizeof(memo));
        cout << dfs(k, a, b, c) << endl;
    }
    return 0;
}