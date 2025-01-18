#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s, ans = "/";
    cin >> s;
    int n = s.size();
    for (int i = 0; i < n; i++) {
        if (s[i] == ']') break;
        if (isupper(s[i])) ans += s[i] - 'A' + 'a';
    }
    cout << ans << endl;
    return 0;
}