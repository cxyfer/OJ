#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL t, x, y, ans;
    cin >> t;
    while (t--) {
        cin >> x >> y;
        if (x < y) {
            if (y & 1) ans = y * y - x + 1;
            else ans = (y - 1) * (y - 1) + x;
        } else {
            if (x & 1) ans = (x - 1) * (x - 1) + y;
            else ans = x * x - y + 1;
        }
        cout << ans << endl;
    }
    return 0;
}