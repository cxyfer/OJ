#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, mx = 0;
    cin >> n;
    string s;
    vector<string> name(n);
    vector<int> cnt(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> name[i] >> s;
        if (s.size() < 3) continue;
        for (int j = 0; j < s.size() - 2; j++) {
            if (s[j] == 's' && s[j + 1] == 'o' && s[j + 2] == 's') {
                cnt[i]++;
            }
        }
        mx = max(mx, cnt[i]);
    }
    for (int i = 0; i < n; i++) {
        if (cnt[i] == mx) {
            cout << name[i] << " ";
        }
    }
    cout << endl << mx << endl;
    return 0;
}