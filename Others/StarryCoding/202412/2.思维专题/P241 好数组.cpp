/*
將 |ai - aj| < ai * aj 轉化為 |1/ai - 1/aj| < 1
- 如果有 0 的話，則需滿足 max(ai) < 1，即 max(1/ai) > 1
- 否則需滿足 max(1/ai) - min(1/ai) < 1
*/

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, a;
    cin >> t;
    while (t--) {
        cin >> n;
        double mx = DBL_MIN, mn = DBL_MAX;
        bool has_zero = false;
        for (int i = 0; i < n; ++i) {
            cin >> a;
            if (a == 0) {
                has_zero = true;
            } else {
                double b = 1.0 / a;
                mx = max(mx, b);
                mn = min(mn, b);
            }
        }
        if (has_zero) cout << (mx > 1 ? "YES" : "NO") << endl;
        else cout << (mx - mn < 1 ? "YES" : "NO") << endl;
    }
    return 0;
}
