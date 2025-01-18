#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 1e9 + 7;
const int N = 20;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int T, C;
    LL n, ans, sigma, cur;
    LL P[N], A[N]; // p_i, a_i
    cin >> T;
    for (int t=1; t<=T; t++) {
        cin >> C;
        for (int i=0; i<C; i++) {
            cin >> P[i] >> A[i];
        }
        ans = 1; n = 1;
        for (int i=0; i<C; i++) {
            sigma = 1; cur = 1;
            for (int j=1; j<=A[i]; j++) {
                cur *= P[i];
                cur %= MOD;
                sigma += cur;
                sigma %= MOD;
            }
            sigma += A[i] * cur % MOD;
            ans *= sigma % MOD;
            ans %= MOD;
            n *= cur;
            n %= MOD;
        }
        ans = (ans + n) % MOD;
        cout << "Case " << t << ": " << ans << endl;
    }
    return 0;
}