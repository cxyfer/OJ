/*
    狀壓DP (Bitmask DP)
*/
#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int n, x;
    cin >> n >> x;
    vector<int> W(n);
    for (int i = 0; i < n; i++) cin >> W[i];
    // 預先計算每個狀態的重量
    sort(W.begin(), W.end());
    vector<int> weights(1 << n, 0);
    for (int i = 0; i < n; i++) { // 初始化只有一個人時的重量
        weights[1 << i] = W[i];
    }
    for (int i = 1; i < (1 << n); i++) { // 透過位運算消除最低位的 1 來計算重量
        weights[i] = weights[i - (i & -i)] + weights[i & -i];
    }
    // 初始化
    int u = (1 << n) - 1; // Universal Set
    // dp[mask] = {rides, subset}, rides 表示已經運行的次數，subset 表示當前搭乘的人的集合
    vector<pair<int, int>> dp(1 << n, {INT_MAX, 0});
    dp[0] = {1, 0};
    for (int mask = 1; mask < (1 << n); mask++) {
        for (int j = 0; j < n; j++) {
            if (mask & (1 << j)) { // 如果 j 還沒搭電梯
                auto [rides, s] = dp[mask ^ (1 << j)];
                // 檢查是否超重
                if (weights[s | (1 << j)] > x) { // 超重了，j 需要搭下一班電梯
                    rides++;
                    s = (1 << j);
                } else { // 沒超重，j 可以搭這班電梯
                    s |= (1 << j);
                }
                // 更新答案
                if (rides < dp[mask].first) { // 次數更少
                    dp[mask] = {rides, s};
                } else if (rides == dp[mask].first && weights[s] < weights[dp[mask].second]) { // 次數相同，但重量更小
                    dp[mask] = {rides, s};
                }
            }
        }
    }
    cout << dp[u].first << endl;
    return 0;
}