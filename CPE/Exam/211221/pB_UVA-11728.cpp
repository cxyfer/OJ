#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int kase = 1, n, ans[N];
    memset(ans, -1, sizeof(ans));
    ans[1] = 1;
    for (int x = 2; x < N; x++) {
        int cur = 1 + x;
        for (int p = 2; p * p <= x; p++) {
            if (x % p == 0) {
                if (p * p == x) cur += p;
                else cur += p + x / p;
            }
        }
        if (cur < N) ans[cur] = x;
    }
    while (cin >> n && n) {
        cout << "Case " << kase++ << ": " << ans[n] << endl;
    }
    return 0;
}