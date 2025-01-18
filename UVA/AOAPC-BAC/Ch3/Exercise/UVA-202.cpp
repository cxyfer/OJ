#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int a, b;
    while (cin >> a >> b) {
        vector<int> ans;
        map<int, int> vis;
        cout << a << "/" << b << " = " << a / b << ".";
        a %= b;
        a *= 10;
        while (!vis.count(a)) {
            vis[a] = ans.size();
            ans.push_back(a / b);
            a %= b;
            a *= 10;
        }
        int n = ans.size();
        for (int i = 0; i < min(50, n); i++) {
            if (i == vis[a]) cout << "(";
            cout << ans[i];
        }
        if (n > 50) cout << "...";
        cout << ")" << endl;
        cout << "   " << n - vis[a] << " = number of digits in repeating cycle" << endl;
        cout << endl;
    }
    return 0;
}