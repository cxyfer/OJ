#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> A(n);
        for (int i = 0; i < n; ++i) cin >> A[i];

        // 不操作
        int ans = 0;
        for (int i = 1; i < n; ++i) {
            ans = gcd(ans, A[i]);
        }

        // 計算前綴和後綴gcd
        vector<int> pre(n + 1), suf(n + 1);
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = gcd(pre[i], A[i]);
        }
        for (int i = n - 1; i >= 0; --i) {
            suf[i] = gcd(suf[i + 1], A[i]);
        }

        // 枚舉替換位置
        for (int i = 0; i < n; ++i) {
            ans = max(ans, gcd(pre[i], suf[i + 1]));
        }
        cout << ans << endl;
    }
    return 0;
}