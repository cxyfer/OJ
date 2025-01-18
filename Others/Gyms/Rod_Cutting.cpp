#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL INF = 0x3f3f3f3f3f3f3f3f;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    vector<LL> P(n + 1);
    for (int i = 1; i <= n; ++i) cin >> P[i];

    vector<LL> f(n + 1, LLONG_MIN / 2);
    f[0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= i; j++) {
            f[i] = max(f[i], P[j] + f[i - j]);
        }
    }
    cout << f[n] << endl;
    return 0;
}