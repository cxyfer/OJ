/*
 * B3637 最长上升子序列
 * https://www.luogu.com.cn/problem/B3637
 */
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

void solve() {
    int n, x;
    cin >> n;
    vector<int> f;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        auto it = lower_bound(f.begin(), f.end(), x);
        if (it == f.end()) f.push_back(x);
        else *it = x;
    }
    cout << f.size() << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    solve();
    return 0;
}