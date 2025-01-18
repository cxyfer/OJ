#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t;
    string s;
    cin >> t;
    cin.ignore(1024, '\n');
    getline(cin, s); // 空行
    while (t--) {
        map<string, int> cnt;
        int tol = 0;
        while (getline(cin, s) && s != "") {
            cnt[s]++;
            tol++;
        }
        for (auto &p : cnt) {
            cout << p.first << " " << fixed << setprecision(4) << p.second * 100.0 / tol << endl;
        }
        if (t) cout << endl;
    }
    return 0;
}