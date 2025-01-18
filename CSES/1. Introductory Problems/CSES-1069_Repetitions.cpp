#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    cin >> s;
    int ans = 1, cur = 1;
    for (int i = 1; i < s.size(); i++) {
        if (s[i] == s[i-1]) {
            cur++;
        } else {
            cur = 1;
        }
        ans = max(ans, cur);
    }
    cout << ans << endl;
    return 0;
}