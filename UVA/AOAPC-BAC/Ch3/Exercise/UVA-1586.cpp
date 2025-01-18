#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    map<char, double> mp = {{'C', 12.01}, {'H', 1.008}, {'O', 16.00}, {'N', 14.01}};
    while (t--) {
        string s;
        cin >> s;
        int i = 0, n = s.size();
        double ans = 0;
        while (i < n) {
            char ch = s[i];
            i++;
            int cur = 0;
            while (i < n && isdigit(s[i])) {
                cur = cur * 10 + (s[i] - '0');
                i++;
            }
            if (!cur) {
                cur = 1;
            }
            ans += mp[ch] * cur;
        }
        cout << fixed << setprecision(3) << ans << endl;
    }
    return 0;
}