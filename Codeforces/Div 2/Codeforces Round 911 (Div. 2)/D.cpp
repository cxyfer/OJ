#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const LL mod = 1e9 + 7;
const int N = 100005;
 
int a[N];
vector<int> b[N];
LL c[N], f[N];
int main() {
    const int wc = 100000;
    for (int i = 1; i <= wc; i++) {
        for (int j = i; j <= wc; j += i) {
            b[j].push_back(i);
        }
    }
    int _;
    scanf("%d", &_);
    while (_--) {
        int n;
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        memset(c, 0, sizeof c);
        memset(f, 0, sizeof f);
        sort(a + 1, a + n + 1);
        for (int i = 1; i <= n; i++) {
            for (auto x : b[a[i]]) {
                f[x] += c[x] * (n - i);
                c[x]++;
            }
        }
        LL ans = 0;
        for (int i = wc; i >= 1; i--) {
            for (int j = i + i; j <= wc; j += i) {
                f[i] -= f[j];
            }
            ans += f[i] * i;
        }
        printf("%lld\n", ans);
    }
    return 0;
}
