/*
    a XOR b < 4 代表除了最低的兩位以外，其他位數都相同
    把能交換的數字分成一組，然後排序，再依序填入原本的位置
*/

#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 2e5 + 5;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int t, n, A[N];
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) cin >> A[i];
        map<int, vector<int>> pos, val;
        for (int i = 0; i < n; i++) {
            pos[A[i] >> 2].push_back(i);
            val[A[i] >> 2].push_back(A[i]);
        }
        vector<int> ans(n);
        for (auto &k : pos) {
            auto &p = k.second;
            auto &v = val[k.first];
            sort(v.begin(), v.end());
            for (int i = 0; i < p.size(); i++) {
                ans[p[i]] = v[i];
            }
        }
        for (int i = 0; i < n; i++) cout << ans[i] << " \n"[i == n - 1];
    }
    return 0;
}