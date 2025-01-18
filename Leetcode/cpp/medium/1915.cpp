/*
 * @lc app=leetcode id=1915 lang=cpp
 * @lcpr version=30122
 *
 * [1915] Number of Wonderful Substrings
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int N = 10;

class Solution {
public:
    /*
        前綴和 + 狀態壓縮
        s << i 表示第 i 個字元是否出現奇數次
        cnt[s] 表示前綴和 s 出現的次數
    */
    long long wonderfulSubstrings(string word) {
        int cnt[1 << N] = {0}; // 前綴和出現次數，初始化為0
        cnt[0] = 1; // 空字串
        int s = 0; // 當前前綴和
        LL ans = 0; // 答案
        for (char ch : word){
            int idx = ch - 'a'; // 當前字元的索引
            s ^= (1 << idx); // 反轉當前字元的出現次數
            ans += cnt[s]; // 只有 s 自身滿足和 s 兩個狀態間所有字元的出現次數都是偶數，即 s ^ s = 0
            for (int i = 0; i < N; i++){
                ans += cnt[s ^ (1 << i)]; // 其中一個字元出現次數是奇數，即 s ^ (s ^ (1 << i)) 只有 1 個 1
            }
            cnt[s] += 1; // 更新前綴和出現次數
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "aba"\n
// @lcpr case=end

// @lcpr case=start
// "aabb"\n
// @lcpr case=end

// @lcpr case=start
// "he"\n
// @lcpr case=end

 */

