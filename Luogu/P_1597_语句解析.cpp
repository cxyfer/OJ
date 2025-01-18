#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    cin >> s;
    vector<int> ans(3, 0);
    int n = s.size(), i = 0;
    while (i < n) {
        int j = i;
        while (j + 1 < n && s[j + 1] != ';') {
            ++j;
        }
        if ('a' <= s[j] && s[j] <= 'c') {
            ans[s[i] - 'a'] = ans[s[j] - 'a'];
        } else {
            ans[s[i] - 'a'] = s[j] - '0';
        }
        i = j + 2;
    }
    cout << ans[0] << ' ' << ans[1] << ' ' << ans[2] << endl;
    return 0;
}