#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int a, b, c, d, L, ans;
    while (cin >> a >> b >> c >> d >> L && (a || b || c || d || L)) {
        ans = 0;
        for (int x = 0; x <= L; ++x) {
            if ((a * x * x + b * x + c) % d == 0) ans++;
        }
        cout << ans << endl;
    }
}