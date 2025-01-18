#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, k;
    cin >> t;
    while (t--) {
        cin >> n >> k;
        vector<int> A(n);
        for (int i = 0; i < n; i++) cin >> A[i];
        int ans = 0;
        auto dfs = [&](auto &&dfs, int i, int s) -> void {
            if (s <= k) ans += 1;
            else return; // Pruning
            // 枚舉下一個選哪個
            for (int j = i; j < n; j++) {
                dfs(dfs, j + 1, s + A[j]);
            }
        };
        dfs(dfs, 0, 0);
        cout << ans << endl;
    }
    return 0;
}