#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x, a;
    cin >> n >> x;
    LL ans = 0, s = 0;
    unordered_map<LL, int> cnt;
    cnt[0] = 1;
    for (int i = 0; i < n; i++) {
        cin >> a;
        s += a;
        ans += cnt[s - x];
        cnt[s]++;
    }
    cout << ans << endl;
    return 0;
}