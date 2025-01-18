#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, tc=1, n, q, r;
    cin >> t;
    while (t--) {
        cin >> n;
        string ans = "";
        while (n) {
            q = n / -2;
            r = n % -2;
            if (r < 0) {
                q += 1;
                r += 2;
            }
            ans += to_string(r);
            n = q;
        }
        reverse(ans.begin(), ans.end());
        cout << "Case #" << tc++ << ": " << (ans.empty() ? "0" : ans) << endl;
    }
    return 0;
}