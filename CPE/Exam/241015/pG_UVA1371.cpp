#include <bits/stdc++.h>
using namespace std;
using LL = long long;
#define endl '\n'

int t;
string x, y;
vector<vector<int>> dp;

bool check(int mid) {
    dp.assign(y.size() + 1, vector<int>(x.size() + 1, 0));
    for (int j = 0; j <= x.size(); j++) {
        dp[0][j] = j;
    }
    for (int i = 1; i <= y.size(); i++) {
        dp[i][0] = i;
        if (dp[i - 1][x.size()] <= mid) {
            dp[i - 1][0] = 0;
        }
        for (int j = 1; j <= x.size(); j++) {
            dp[i][j] = min({dp[i - 1][j] + 1, 
                            dp[i][j - 1] + 1, 
                            dp[i - 1][j - 1] + (x[j - 1] == y[i - 1] ? 0 : 1)});
        }
    }
    return dp[y.size()][x.size()] <= mid;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    cin >> t;
    while (t--) {
        cin >> x >> y;

        int left = 0, right = x.size();
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        cout << left << endl;
    }
    return 0;
}