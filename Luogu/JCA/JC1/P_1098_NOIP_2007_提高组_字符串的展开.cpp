#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int p1, p2, p3;
    string s;
    cin >> p1 >> p2 >> p3 >> s;
    int n = s.size();
    string ans = "";
    for (int i = 0; i < n; i++) {
        char ch = s[i];
        char pre = (i > 0) ? ans.back() : '#';
        char suf = (i + 1 < n) ? s[i + 1] : '#';
        if (ch == '-' && pre < suf && (islower(pre) && islower(suf) || isdigit(pre) && isdigit(suf))) {
            string tmp = "";
            if (p1 == 1) {
                for (char k = pre + 1; k < suf; k++) {
                    tmp += string(p2, k);
                }
            } else if (p1 == 2) {
                for (char k = pre + 1; k < suf; k++) {
                    tmp += string(p2, toupper(k));
                }
            } else {
                tmp += string((suf - pre - 1) * p2, '*');
            }
            if (p3 == 1) {
                ans += tmp;
            } else {
                ans += string(tmp.rbegin(), tmp.rend());
            }
        } else {
            ans += ch;
        }
    }
    cout << ans << endl;
    return 0;
}