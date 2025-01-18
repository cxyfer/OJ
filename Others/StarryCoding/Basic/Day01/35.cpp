#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e5 + 5;
#define endl '\n'

int a[N], w[N];
LL s[N];

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 1; i <= n; i++) cin >> a[i];
        for (int i = 1; i <= n; i++) cin >> w[i];
        // for (int i = 1; i <= n; i++) { // Prefix sum
        //     s[i] = s[i - 1] + (a[i] ? -w[i] : w[i]);
        // }
        LL ans = 0; // Initial answer
        for (int i = 1; i <= n; i++) ans += a[i] * w[i];
        // LL mn = 0, added = 0;
        LL mx = 0, added = 0;
        for (int i = 1; i <= n; i++) {
            // added = max(added, s[i] - mn);
            // mn = min(mn, s[i]);
            mx = max(0LL, mx + (a[i] ? -w[i] : w[i]));
            added = max(added, mx);
        }
        cout << ans + added << endl;
    }
    return 0;
}