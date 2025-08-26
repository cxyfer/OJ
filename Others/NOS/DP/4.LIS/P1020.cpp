/*
P1020 [NOIP 1999 提高组] 导弹拦截
https://www.luogu.com.cn/problem/P1020

第一問：求最長非嚴格遞減子序列長度
- 1. 直接逆過來求最長非嚴格遞增子序列
- 2. 用負數
第二問：求最長嚴格遞增子序列長度
*/
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#define endl '\n'

void solve() {
    int x;
    vector<int> A;
    while (cin >> x) A.push_back(x);
    int n = A.size();

    vector<int> f;
    for (auto x : A | views::reverse) {
        auto it = upper_bound(f.begin(), f.end(), x);
        if (it == f.end()) f.push_back(x);
        else *it = x;
    }
    cout << f.size() << endl;

    f.clear();
    for (auto x : A) {
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