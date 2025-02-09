#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    cin >> s;
    int n = s.size();
    int ans = 0, i = 0;
    while (i < n) {
        if (s.substr(i, 5) == "luogu") {
            ans++;
            i += 5;
        } else {
            i++;
        }
    }
    cout << ans << endl;
    return 0;
}