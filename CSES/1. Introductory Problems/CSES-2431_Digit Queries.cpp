/* CSES-2431 Digit Queries
    預處理長度為 x (x位數) 的數字總共佔據幾個字元，並以此求出目標是第幾個幾位數的第幾個字元。
    C++ 在算 pow(10, i) 時，i 過大會有精度問題，因此用 ppow[i] 來存 10^i。
*/
#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 20;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL t, q, i, cur = 1;
    cin >> t;
    LL cnt[N] = {0}, ppow[N] = {0};
    for (int i = 1; i < N; i++) {
        cnt[i] = 9 * cur * i;
        ppow[i-1] = cur;
        cur *= 10;
    }
    while (t--) {
        cin >> q;
        for (i = 1; i < N; i++) {
            if (q <= cnt[i]) break;
            q -= cnt[i];
        }
        q--; // i 位數的第 q 個字元 (0-indexed)
        LL x, y;
        x = q / i; y = q % i; // i 位數的第 x 個數字的第 y 個字元 (0-indexed)
        LL ans = ppow[i-1] + x;
        cout << to_string(ans)[y] << endl;
    }
    return 0;
}