/*
 * @lc app=leetcode id=3144 lang=cpp
 *
 * [3144] Minimum Substring Partition of Equal Character Frequency
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int N = 1005;
const int INF = 0x3f3f3f3f;

class Solution {
public:
    /*
        劃分型 DP，預處理出以 i 開頭的平衡點 j
        賽時處理是否為平衡點的方法比較粗糙，達到了 O(26 n^2)，用 Python 吃了 TLE (但是 C++ 能過)
        這裡是用 O(1) 的方式更新 mx 和判斷是否為平衡點，所以是 O(n^2)
        - 由於會變大的數只有一個，所以更新 mx 時只要檢查 s[j] 的次數即可
        - 如果是平衡點，則字母數 len(cnt) 乘上最大次數 mx 等於子串長度 j - i + 1

        Reference:
        - https://leetcode.cn/circle/discuss/tb4PG6/
    */
    int dp[N];
    int dfs(int i, string &s) {
        if (i == s.size()) return 0;
        if (dp[i] != -1) return dp[i];
        int res = INF, mx = 0, cnt[26] = {0}; 
        for (int j = i; j < s.size(); j++) {
            cnt[s[j] - 'a'] += 1;
            mx = max(mx, cnt[s[j] - 'a']); // 由於變大數只有一個，所以只要檢查 s[j] 的次數即可
            int sz = 0;
            for (int k = 0; k < 26; k++) if (cnt[k]) sz++;
            if (j - i + 1 == mx * sz)
                res = min(res, 1 + dfs(j + 1, s));
        }
        return dp[i] = res;
    }

    int minimumSubstringsInPartition(string s) {
        memset(dp, -1, sizeof(dp));
        return dfs(0, s);
    }
};
// @lc code=end
