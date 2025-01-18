#include <bits/stdc++.h>
using namespace std;
const int MX = 180;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        vector<int> cnt(10);
        for (char ch : s) {
            cnt[ch - '0']++;
        }
        int tot = 0;
        for (int i = 1; i <= 9; i++) {
            tot = (tot + i * cnt[i]) % 9;
        }
        if (tot == 0) {
            cout << "YES" << endl;
            continue;
        }
        vector<bool> f(MX + 1);
        f[0] = true;
        for (int x : {2, 3}) {
            int d = x * x - x;
            for (int i = 0; i < cnt[x]; i++) {
                for (int j = MX; j >= d; j--) {
                    if (f[j - d]) f[j] = true;
                }
            }
        }
        int t = 9 - tot;
        while (t <= MX && !f[t]) t += 9;
        cout << (t <= MX ? "YES" : "NO") << endl;
    }
    return 0;
}