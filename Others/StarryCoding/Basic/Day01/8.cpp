#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 1e5 + 5;
#define endl '\n'

LL A[N], diff[N], s[N];

/*
    diff <-> A <-> prefix sum
*/
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    LL n, p, q, l, r, x;
    cin >> n >> p >> q;
    for (int i = 1; i <= n; i++) cin >> A[i];
    for (int i = 1; i <= n; i++) diff[i] = A[i] - A[i - 1];
    while (p--){
        cin >> l >> r >> x;
        diff[l] += x;
        diff[r + 1] -= x;
    }
    for (int i = 1; i <= n; i++) A[i] = A[i - 1] + diff[i]; // 還原
    for (int i = 1; i <= n; i++) s[i] = s[i - 1] + A[i]; // Prefix Sum
    while (q--) {
        cin >> l >> r;
        cout << s[r] - s[l - 1] << endl;
    }
    return 0;
}