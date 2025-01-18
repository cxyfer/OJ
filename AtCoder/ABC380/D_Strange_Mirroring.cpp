#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const LL MAX_LN = 1e18;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s; cin >> s;
    int n = s.size();
    int q; cin >> q;
    vector<LL> ln = {n};
    while (ln.back() <= MAX_LN) ln.push_back(ln.back() * 2);
    reverse(ln.begin(), ln.end());
    while (q--) {
        LL k; cin >> k;
        int cnt = 0;
        for (auto &x : ln) {
            if (k > x) {
                k -= x;
                cnt++;
            }
        }
        char ch = s[k - 1];
        if (cnt & 1) ch = islower(ch) ? toupper(ch) : tolower(ch);
        cout << ch << " ";
    }
    cout << endl;
    return 0;
}