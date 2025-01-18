#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const LL mod = 1e9 + 7;
const int N = 1000005;
 
LL a[N], b[N];
int main() {
    int n, q;
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; i++) {
        scanf("%lld", &b[i]);
    }
    while (q--) {
        for (int i = 1; i <= n; i++) a[i] = b[i];
        LL m;
        scanf("%lld", &m);
        LL ans = 0;
        for (int k = 59; k >= 0; k--) {
            LL s = 0;
            for (int i = 1; i <= n; i++) {
                if (a[i] >> k & 1 ^ 1)
                    s += (1LL << k) - a[i];
                if (s > m) break;
            }
            if (m >= s) {
                m -= s;
                ans += 1LL << k;
                for (int i = 1; i <= n; i++) {
                    if (a[i] >> k & 1 ^ 1) a[i] = 0;
                }
            }
            for (int i = 1; i <= n; i++)
                if (a[i] >> k & 1) a[i] ^= 1 << k;
        }
        printf("%lld\n", ans);
    }
    return 0;
}