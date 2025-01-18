#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n;
    LL mn = 0, s = 0, ans = LLONG_MIN;
    for (int i = 0; i < n; i++) {
        cin >> x;
        s += x;
        ans = max(ans, s - mn);
        mn = min(mn, s);
    }
    cout << ans << endl;
    return 0;
}