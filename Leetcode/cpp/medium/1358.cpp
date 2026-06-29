/*
 * @lc app=leetcode.cn id=1358 lang=cpp
 *
 * [1358] 包含所有三种字符的子字符串数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        int ans = 0, left = 0, need = 3;
        vector<int> cnt(3);
        for (char& ch : s) {
            // 1. 入窗口
            if (++cnt[ch - 'a'] == 1) need--;
            // 2. 出窗口，維持窗口在向左延伸即可滿足條件的狀態
            while (need == 0) {
                if (--cnt[s[left] - 'a'] == 0) need++;
                left++;
            }
            // 3. 累加答案，此時 [0, left - 1] 都是合法的左端點
            ans += left;
        }
        return ans;
    }
};
// @lc code=end

