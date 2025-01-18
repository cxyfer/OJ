#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, m;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        vector<LL> A(n), B(m);
        for (int i = 0; i < n; i++) cin >> A[i];
        for (int i = 0; i < m; i++) cin >> B[i];
        sort(A.begin(), A.end(), greater<LL>());
        sort(B.begin(), B.end(), greater<LL>());
        LL target = 0;
        for (int i = 0; i < m; i++) target += A[i] * B[i];
        target /= 2;
        int ans = 0;
        // 考慮到第 i 名學生，以 j 表示已選座位的狀態，當前總和為 s
        auto dfs = [&](auto &&dfs, int i, int j, LL s) -> void {
            if (i == m) {
                if (s >= target) ans += 1;
                return;
            }
            for (int k = 0; k < n; k++) { // 枚舉這個學生坐哪個位置
                if (j & (1 << k)) continue;
                dfs(dfs, i + 1, j | (1 << k), s + A[k] * B[i]);
            }
        };
        dfs(dfs, 0, 0, 0);
        cout << ans << endl;
    }
    return 0;
}