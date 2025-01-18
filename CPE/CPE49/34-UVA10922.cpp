#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
#define endl '\n'

int dfs(string n) {
    int s = 0;
    for (char ch : n) {
        s += ch - '0';
    }
    if (n.size() == 1 && s != 9) {
        return -INF;
    }
    if (s == 9) {
        return 1;
    }
    return 1 + dfs(to_string(s));
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string n;
    while (cin >> n && n != "0") {
        int ans = dfs(n);
        if (ans < 0) {
            cout << n << " is not a multiple of 9." << endl;
        } else {
            cout << n << " is a multiple of 9 and has 9-degree " << ans << "." << endl;
        }
    }
    return 0;
}