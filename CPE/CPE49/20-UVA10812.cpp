#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, s, d, a, b;
    cin >> t;
    while (t--) {
        cin >> s >> d;
        a = (s + d) / 2;
        b = s - a;
        if ((s + d) & 1 || a < 0 || b < 0 ) cout << "impossible" << endl;
        else cout << a << " " << b << endl;
    }
    return 0;
}