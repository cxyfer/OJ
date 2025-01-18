#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

LL qpow(LL a, LL b, LL p) {
    LL res = 1;
    while (b) {
        if (b & 1) res = res * a % p;
        a = a * a % p;
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, p;
    cin >> n >> p;
    // minpf[i] 表示 i 的最小質因數，若 i 為質數，則 minpf[i] = 0
    vector<int> minpf(2 * n + 1, 0);
    for (int i = 2; i <= 2 * n; ++i)
        if (minpf[i] == 0)
            for (int j = i * 2; j <= 2 * n; j += i)
                if (minpf[j] == 0)
                    minpf[j] = i;

    // 因子計數法
    vector<int> cnt(2 * n + 1, 0);
    fill(cnt.begin() + 1, cnt.begin() + n + 1, -1);
    fill(cnt.begin() + n + 2, cnt.end(), 1);
    for (int i = 2 * n; i > 1; i--) {
        if (minpf[i] != 0) {
            cnt[minpf[i]] += cnt[i];
            cnt[i / minpf[i]] += cnt[i];
            cnt[i] = 0;
        }
    }
    // 根據剩下的質因數計算結果
    LL ans = 1;
    for (int i = 2; i <= 2 * n; i++)
        if (cnt[i] != 0)
            ans = ans * qpow(i, cnt[i], p) % p;
    cout << ans << endl;
    return 0;
}