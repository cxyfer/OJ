/*
UVA-10690 Expression Again
https://vjudge.net/problem/UVA-10690

由於 N + M 的數量可以到 110，回溯法會 TLE
注意到 A[i] 的值域很小，可以用 DP 維護可以透過 k 個元素組合出來的和
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int N, M;
    while (cin >> N >> M) {
        vector<int> A(N + M);
        for (auto &x : A) cin >> x;

        int k = min(N, M);
        int tot = accumulate(A.begin(), A.end(), 0);

        // f[k] 表示可以透過 k 個元素組合出來的和
        vector<unordered_set<int>> f(k + 1);
        f[0].insert(0);
        for (auto &x : A)
            for (int i = k - 1; i >= 0; i--)
                for (auto &y : f[i])
                    f[i + 1].insert(y + x);
        
        int mx = INT_MIN, mn = INT_MAX;
        for (auto &y : f[k]) {
            int v = y * (tot - y);
            mx = max(mx, v);
            mn = min(mn, v);
        }
        cout << mx << " " << mn << endl;

    }
    return 0;
}