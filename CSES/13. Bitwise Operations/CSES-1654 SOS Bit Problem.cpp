/*
CSES-1654 SOS Bit Problem
https://cses.fi/problemset/task/1654
Sum over Subsets (SOS) DP 模板題

1. 滿足 (x | y) == x 的 y 個數：x 的子集(subset)中的元素數量
2. 滿足 (x & y) == x 的 y 個數：x 的超集(superset)中的元素數量
3. 滿足 (x & y) != 0 的 y 個數：
  - 正難則反，所求為全部元素數量 n 減去 (x & y) == 0 的 y 個數
  - 而滿足 (x & y) == 0 的 y 個數，等價於 (~x | y) == (~x) 的 y 個數，故由 1. 可得

轉移順序說明：
以子集和為例，當枚舉到第 i 位（或第 i 維）時，一定是從該位為 0 的位置轉移而來，
因此在計算第 i 位時，轉移來源一定不會被修改過，
故可以從小到大或從大到小皆可，計算超集和時同理。
*/
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
#define endl '\n'

void solve() {
    int n; cin >> n;
    vector<int> A(n);
    for (auto &x : A) cin >> x;
    int B = bit_width(static_cast<unsigned>(ranges::max(A)));
    int U = 1 << B;
    vector<int> f1(U), f2(U);
    for (auto &x : A) {
        f1[x]++;
        f2[x]++;
    }
    for (int i = 0; i < B; i++) {
        for (int s = 0; s < U; s++) {
            s |= (1 << i);
            f1[s] += f1[s ^ (1 << i)];
            f2[s ^ (1 << i)] += f2[s];
        }
    }
    for (auto &x : A)
        cout << f1[x] << ' ' << f2[x] << ' ' << n - f1[x ^ ((1 << B) - 1)] << endl;
    return;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    solve();
    return 0;
}