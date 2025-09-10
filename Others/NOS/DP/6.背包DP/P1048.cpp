/*
P1048 [NOIP 2005 普及组] 采药
https://www.luogu.com.cn/problem/P1048
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int T, M;
    cin >> T >> M;
    vector<pair<int, int>> items(M);
    for (int i = 0; i < M; i++) cin >> items[i].first >> items[i].second;
    vector<int> f(T + 1, 0);
    for (auto [t, v] : items)
        for (int j = T; j >= t; j--) f[j] = max(f[j], f[j - t] + v);
    cout << f[T] << endl;
    return 0;
}