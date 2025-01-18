#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, st, ed;
    cin >> n;
    map<int, int> d;
    for (int i = 0; i < n; i++) {
        cin >> st >> ed;
        d[st]++;
        d[ed]--;
    }
    int ans = 0, cur = 0;
    for (auto &[k, v]: d) {
        cur += v;
        ans = max(ans, cur);
    }
    cout << ans << endl;
    return 0;
}