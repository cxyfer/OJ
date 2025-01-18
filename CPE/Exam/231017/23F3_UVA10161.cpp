#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL n, m, no, x, y;
    while (cin >> n) {
        if (n == 0) break;
        m = sqrt(n);
        if (m * m < n) m += 1;
        no = m * m - n + 1;
        if (no < m) {
            x = (m & 1) ? no : m;
            y = (m & 1) ? m : no;
        } else if (no > m) {
            x = (m & 1) ? m : m - (no - m);
            y = (m & 1) ? m - (no - m) : m;
        } else {
            x = m; y = m;
        }
        cout << x << ' ' << y << endl;
    }
    return 0;
}