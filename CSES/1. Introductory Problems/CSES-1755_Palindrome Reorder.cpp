#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s;
    cin >> s;
    int cnt[26] = {0};
    for (char ch : s) {
        cnt[ch - 'A']++;
    }
    bool flag = true;
    string ans = "", mid = "";
    for (int i = 0; i < 26; i++) {
        char ch = i + 'A';
        if (cnt[i] & 1) {
            if (mid != "") {
                flag = false;
                break;
            }
            mid = ch;
        }
        ans += string(cnt[i] / 2, ch);
    }
    if (!flag) {
        cout << "NO SOLUTION" << endl;
    } else {
        cout << ans + mid + string(ans.rbegin(), ans.rend()) << endl;
    }
    return 0;
}