/*
P12379 [蓝桥杯 2023 省 Python B] 松散子序列
https://www.luogu.com.cn/problem/P12379
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    string s; cin >> s;
    int n = s.size();
    vector<int> f(n + 1);
    for (int i = 1; i <= n; i++) {
        int v = s[i - 1] - 'a' + 1;
        f[i] = max(f[i - 1], (i > 1 ? f[i - 2] : 0) + v);
    }
    cout << f[n] << endl;
    return 0;
}