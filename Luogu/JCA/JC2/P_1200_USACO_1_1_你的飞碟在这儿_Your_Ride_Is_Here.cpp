#include <bits/stdc++.h>
using namespace std;
const int MOD = 47;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s, t;
    cin >> s >> t;
    int x = 1, y = 1;
    for (auto ch : s) x = x * (ch - 'A' + 1) % MOD;
    for (auto ch : t) y = y * (ch - 'A' + 1) % MOD;
    cout << (x == y ? "GO" : "STAY") << endl;
    return 0;
}