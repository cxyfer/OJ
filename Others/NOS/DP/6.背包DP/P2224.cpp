/*
P2224 [HNOI2001] 产品加工
https://www.luogu.com.cn/problem/P2224
背包DP：將其中一維視為 weight，另一維視為 value
*/
#include <bits/stdc++.h>
using namespace std;
const int MAX_T = 3e4 + 5;
#define endl '\n'

void solve() {
    int N; cin >> N;

    vector<tuple<int, int, int>> items(N);
    for (auto &[a, b, c] : items) cin >> a >> b >> c;

    // f[t1] 表示第一台機器工作 t1 時間時，第二台機器的最小工作時間
    vector<int> f(MAX_T, INT_MAX / 2);
    f[0] = 0;
    int s = 0;
    for (auto [a, b, c] : items) {
        s += max(a, c);  // 限制當前枚舉的上界
        for (int t1 = s; t1 >= 0; --t1) {
            int t2 = INT_MAX / 2;
            if (a > 0 && t1 - a >= 0) t2 = min(t2, f[t1 - a]);
            if (b > 0) t2 = min(t2, f[t1] + b);
            if (c > 0 && t1 - c >= 0) t2 = min(t2, f[t1 - c] + c);
            f[t1] = t2;
        }
    }

    int ans = INT_MAX / 2;
    for (int t1 = 0; t1 <= s; ++t1)
        ans = min(ans, max(t1, f[t1]));
    cout << ans << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}