/*
 * @lc app=leetcode.cn id=2266 lang=cpp
 *
 * [2266] 统计打字方案数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
using LL = long long;
class Solution {
public:
    /*
        動態規劃 + 分組循環 + 乘法原理
    */
    int countTexts(string pressedKeys) {
        int n = pressedKeys.size();
        vector<LL> dp3 = {1, 1, 2, 4}, dp4 = {1, 1, 2, 4};
        for (int i = 4; i <= n; i++) {
            dp3.push_back((dp3[i - 1] + dp3[i - 2] + dp3[i - 3]) % MOD);
            dp4.push_back((dp4[i - 1] + dp4[i - 2] + dp4[i - 3] + dp4[i - 4]) % MOD);
        }
        LL ans = 1;
        for (int i = 0; i < n; ) { // 分組循環
            int st = i;
            i++;
            while (i < n && pressedKeys[i] == pressedKeys[i - 1]) {
                i++;
            }
            ans = (ans * (pressedKeys[i - 1] == '7' || pressedKeys[i - 1] == '9' ? dp4[i - st] : dp3[i - st])) % MOD;
        }
        return ans % MOD;
    }
};
// @lc code=end

