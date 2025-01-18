#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int MOD = 1e9 + 7;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL t, n, k;
    cin >> t;
    unordered_map<LL, tuple<LL, LL, vector<LL>>> pisano;
    pisano[1] = {1, 1, {1}};
    while (t--) {
        cin >> n >> k;
        if (pisano.find(k) == pisano.end()) {
            LL f_pre = 1, f_cur = 1;
            vector<LL> pos;
            LL i = 1;
            while (true) {
                if (f_pre % k == 0) {
                    pos.push_back(i);
                }
                LL tmp = f_pre;
                f_pre = f_cur;
                f_cur = (tmp + f_cur) % k;
                i++;
                if (f_pre == 1 && f_cur == 1) {
                    break;
                }
            }
            pisano[k] = {i-1, pos.size(), pos};
        }
        auto [ln, cnt, pos] = pisano[k];
        if (cnt == 0) {
            cout << -1 << endl;
            continue;
        }
        LL q = n / cnt;
        LL r = n % cnt;
        if (r == 0) {
            cout << (q * ln) % MOD << endl;
        } else {
            cout << ((q * ln) % MOD + pos[r-1]) % MOD << endl;
        }
    }
    return 0;
}