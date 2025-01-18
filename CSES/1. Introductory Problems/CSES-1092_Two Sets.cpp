#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL n; cin >> n;
    LL s = n * (n + 1) / 2;
    LL s1 = s / 2, s2 = s / 2;
    vector<int> res1, res2;
    if (s & 1) {
        cout << "NO" << endl;
    }
    else {
        for (int x = n; x > 0; x--) {
            if (s1 - x >= 0) {
                res1.push_back(x);
                s1 -= x;
            }
            else {
                res2.push_back(x);
                s2 -= x;
            }
        }
        cout << "YES" << endl;
        cout << res1.size() << endl;
        for (int i = 0; i < res1.size(); i++) {
            cout << res1[i] << (i == res1.size() - 1 ? endl : ' ');
        }
        cout << res2.size() << endl;
        for (int i = 0; i < res2.size(); i++) {
            cout << res2[i] << (i == res2.size() - 1 ? endl : ' ');
        }
    }
    return 0;
}