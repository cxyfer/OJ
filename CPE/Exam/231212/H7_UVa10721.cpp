#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int N = 55;
#define endl '\n'

LL dp[N][N][N];

LL BC(int n, int k, int m) {
    if (dp[n][k][m] != -1) return dp[n][k][m]; // memoization
    if (n == 0) return k == 0; // 沒有unit了，若還有bar則不滿足
    if (k == 1) return n <= m; // 只有1個bar，若滿足限制條件則有1種可能
    LL res = 0;
    for (int x = 1; x <= min(n, m); ++x) {
        res += BC(n-x, k-1, m); // 剩下n-x個units, k-1個bars, 每個bar最多還是m個units
    }
    dp[n][k][m] = res;
    return res;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, k, m;
    memset(dp, -1, sizeof(dp));
    while (cin >> n >> k >> m) {
        cout << BC(n, k, m) << endl;
    }
    return 0;
}