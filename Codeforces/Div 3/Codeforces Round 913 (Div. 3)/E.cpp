#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const LL mod = 1e9 + 7;
const int N = 300005;
 
char s[N];
 
int c[20][20];
int main() {
    for (int i = 0; i <= 15; ++i) {
        c[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            c[i][j] = c[i - 1][j] + c[i - 1][j - 1];
        }
    }
    int _;
    scanf("%d", &_);
    while (_--) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            printf("1\n");
            continue;
        }
        LL ans = 1;
        while (n) {
            int x = n % 10;
            ans = ans * c[x + 2][2];
            n /= 10;
        }
        printf("%lld\n", ans);
    }
    return 0;
}