#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, target, n;
    cin >> t;
    while (t--) {
        cin >> target >> n;

        vector<int> bars(n);
        for (int i = 0; i < n; ++i) cin >> bars[i];
        vector<bool> dp(target + 1, false);

        dp[0] = true;
        for (int bar : bars) {
            for (int i = target; i >= bar; --i) {
                dp[i] = dp[i] | dp[i - bar];
            }
        }

        cout << (dp[target] ? "YES" : "NO") << endl;
    }
    return 0;
}