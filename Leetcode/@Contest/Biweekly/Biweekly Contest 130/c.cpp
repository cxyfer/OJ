#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
const int INF = 0x3f3f3f3f;

class Solution {
public:
    int dp[N];

    int dfs(int i, string &s) {
        if (i == s.size()) return 0;
        if (dp[i] != -1) return dp[i];
        int ans = INF, cnt[26] = {0}; 
        int mx, mn;
        for (int j = i; j < s.size(); j++) {
            cnt[s[j] - 'a'] += 1;
            mx = -INF, mn = INF;
            for (int k = 0; k < 26; k++) {
                if (cnt[k]) {
                    mx = max(mx, cnt[k]);
                    mn = min(mn, cnt[k]);
                }
            }
            if (mx == mn)
                ans = min(ans, 1 + dfs(j + 1, s));
        }
        return dp[i] = ans;
    }

    int minimumSubstringsInPartition(string s) {
        memset(dp, -1, sizeof(dp));
        return dfs(0, s);
    }
};