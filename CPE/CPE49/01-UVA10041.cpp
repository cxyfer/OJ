#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> s(n);
        for (auto &x: s) cin >> x; // read input
        sort(s.begin(), s.end()); // sort
        int mid = n / 2;
        LL ans = 0;
        for (auto &x: s) ans += abs(x - s[mid]);
        cout << ans << endl;
        
    }
    return 0;
}